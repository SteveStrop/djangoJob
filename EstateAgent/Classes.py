import re


class Address:
    """
    Store a UK address passed as postcode and street etc. parts
    """
    POSTCODE_REGEXP = r'[A-Z]{1,2}[\dR][\dA-Z]? [\d][A-Z]{2}'

    def __init__(self, street=None, postcode=""):
        """
        :param street:  string
        :param postcode: string
        """

        self.street = street
        self.postcode = self.__validate_postcode__(postcode)

    @staticmethod
    def __validate_postcode__(postcode):
        """
        Convert input to upper case then check if it is a valid mainland UK postcode
        :param postcode: string
        :return string : valid uppercase postcode or None
        """
        try:
            postcode = postcode.upper()  # catches non string postcodes as well
            return re.fullmatch(Address.POSTCODE_REGEXP, postcode)[0]
        except (AttributeError, TypeError):
            return None

    def __str__(self):
        """
        String representation of Address object.
        :return: string
        """
        return f"{self.street}, {self.postcode}" if self.street else ""


class Appointment:
    """
    Store appointment date and time in 24h format
    """

    TIME_FORMAT = "%a %d %b @ %H:%M"  # datetime formatting Ddd dd Mmm @ HH:MM

    def __init__(self, address=Address(None), dtime=None):
        """
        :param address: Address object
        :param dtime:   Datetime object
        """

        self.address = address
        self.date = dtime

    def __str__(self):
        """
        Display Appointment date / time  in 'Day dd Mmm @ hh:mm' format or 'TBA' if none set
        :return: string
        """
        try:
            return self.date.strftime(Appointment.TIME_FORMAT)
        except (TypeError, AttributeError):
            return "TBA"


class Client:
    """
    Stores contact details for clients.
    Clients may have websites where they list details of jobs.
    If so, then separate Scraper & Parser objects must be created along with a ConfigXX file (XX denotes the client).
    These allow parsing of the jobs into Job objects (defined below) for saving to the database.
    """

    def __init__(self, name_1=None, name_2=None, phone_1=None, phone_2=None, phone_3=None, notes=None):
        """
        :param name_1:  string
        :param name_2:  string
        :param phone_1:  string
        :param phone_2: string
        :param phone_3: string
        :param notes:   string
    """

        self.name_1 = name_1
        self.name_2 = name_2
        self.phone_1 = self.validate_tel(phone_1)
        self.phone_2 = self.validate_tel(phone_2)
        self.phone_3 = self.validate_tel(phone_3)
        self.notes = notes

    def validate_tel(self, tel):
        """ Check tel is a valid UK phone number and return correctly formatted version or None
        :param tel : string
        :return string or None"""
        try:
            tel_digits, tel_format = self.__get_tel_format__(tel)
            return self.__format_tel__(tel_digits, tel_format)
        except TypeError:
            return None

    @staticmethod
    def __get_tel_format__(tel):

        """
        Strip out non digits from 'tel'
        Get the correct space-delimited format for corresponding 'tel' or None if no match
        Return digit only version of tel and it's corresponding format
        :param tel: string
        :return: string , string
        """
        tel_formats = [
                ("01### ##### ", "01\d{8}"),
                ("01### ### ###", "01\d{9}"),
                ("011# ### ####", "011\d{8}"),
                ("01#1 ### ####", "01\d1\d{7}"),
                ("013397 #####", "013397\d{5}"),
                ("013398 #####", "013398\d{5}"),
                ("013873 #####", "013873\d{5}"),
                ("015242 #####", "015242\d{5}"),
                ("015394 #####", "015394\d{5}"),
                ("015395 #####", "015395\d{5}"),
                ("015396 #####", "015396\d{5}"),
                ("016973 #####", "016973\d{5}"),
                ("016974 #####", "016974\d{5}"),
                ("016977 #### ", "016977\d{4}"),
                ("016977 #####", "016977\d{5}"),
                ("017683 #####", "017683\d{5}"),
                ("017684 #####", "017684\d{5}"),
                ("017687 #####", "017687\d{5}"),
                ("019467 #####", "019467\d{5}"),
                ("019755 #####", "019755\d{5}"),
                ("019756 #####", "019756\d{5}"),
                ("02# #### ####", "02\d{9}"),
                ("03## ### ####", "03\d{9}"),
                ("05### ### ###", "05\d{9}"),
                ("07### ### ###", "07\d{9}")
        ]

        try:
            # strip non digits
            tel = "".join([n for n in tel if n.isdigit()])
        except TypeError:
            return None

        tel_format = None
        # compare regexp in tel_formats with tel
        for fmt, regexp in tel_formats:  # search them all because the last match is the one we want
            try:
                tel = re.fullmatch(regexp, tel)[0]
                tel_format = fmt
            except (TypeError, AttributeError):
                continue  # loop if no match
        return tel, tel_format

    @staticmethod
    def __format_tel__(phone, template):
        """
        Format the digit only string to match template by adding spaces.
        Return correctly formatted UK phone number
        :param phone: string
        :param template: string
        :return: string
        """
        try:
            assert isinstance(phone, str) and isinstance(template, str)
        except AssertionError:
            return None  # not a valid UK phone number
        # cast phone to a list
        phone = list(phone)
        # build correctly formatted phone by popping first select_drop if matching template character is non blank
        # strip any whitespace
        return "".join([phone.pop(0) if c != " " else " " for c in template]).strip()

    def __str__(self):
        name1 = f"Primary contact:   {self.name_1:30.40}" if self.name_1 else ""
        phone1 = f"Tel: {self.phone_1:>13.13}" if self.phone_1 else ""
        name2 = f"\nSecondary contact: {self.name_2:30.40}" if self.name_2 else ""
        phone2 = f"Tel: {self.phone_2:>13.13}" if self.phone_2 else ""
        name3 = f"\nOther contact:     {' ':30.40}" if self.phone_3 else ""
        phone3 = f"Tel: {self.phone_3:>13.13}" if self.phone_3 else ""

        return f"{name1} {phone1}" \
            f"{name2} {phone2}" \
            f"{name3} {phone3}"


class Vendor(Client):
    def __init__(self, name_1=None, name_2=None, phone_1=None, phone_2=None, phone_3=None, notes=None):
        super().__init__(name_1, name_2, phone_1, phone_2, phone_3, notes)


class Agent(Client):
    def __init__(self, name_1=None, name_2=None, phone_1=None, phone_2=None, phone_3=None, notes=None, address=None,
                 branch=None):
        """
        :param name_1: string
        :param name_2: string
        :param phone_1: string
        :param phone_2: string
        :param phone_3: string
        :param notes: string
        :param address: Address object
        :param branch string
        """
        super().__init__(name_1, name_2, phone_1, phone_2, phone_3, notes)
        self.address = address
        self.branch = branch

    def __str__(self):
        return self.branch if self.branch else ''


class Job:
    """
    Holds all data that completely describes a job from any config.
    Note not all clients require all attributes to contain valid data
    A Job contains all information needed to successfully carry out a photoshoot of a house for sale.
    It references:
    Job.ref (primary key in database later (?)
    The commissioning Client
    The Agent selling the house on behalf of the Vendor
    The Appointment details: Address and time
    The local folder where taken photos are stored  (os.path object)
    The job status (active / archived)
    """
    ACTIVE = 1
    ARCHIVED = 0

    def __init__(self, ref=None, client=Client(None), agent=Agent(None), vendor=None, beds=None, property_type=None,
                 appointment=Appointment(address=Address(None)), folder=None, notes=None, floorplan=True, photos=0,
                 specific_reqs=None, system_notes=None):
        """
        :param ref:            string
        :param client:         Client object
        :param agent:          Agent object
        :param appointment:    Appointment object consisting of Address object and time
        :param folder:         os.path object
        :param: floorplan:     boolean
        :param: photos:        int
        :param: specific_reqs: dict {req : quantity}

        """
        self.ref = ref
        self.client = client
        self.agent = agent
        self.vendor = vendor
        self.appointment = appointment
        self.property_type = property_type
        self.beds = beds
        self.notes = notes
        self.floorplan = floorplan
        self.photos = photos
        self.folder = folder
        self.specific_reqs = specific_reqs
        self.status = Job.ACTIVE
        self.system_notes = system_notes
        # todo possible add references to links on webpage for various bits and pieces

    def set_appointment_date(self, time, time_format):
        """"
        Set job appointment date and time as datetime objects
        :param time :        datetime object
        :param time_format : Datetime format
        :return bool
        """
        # assert isinstance(dt.datetime,time)
        # todo implement this
        # self.appointment.date = dt.datetime.
        # self.appointment.time =
        return self.appointment.date and self.appointment.time

    def set_appointment_address(self, address, postcode):
        """" Set job appointment address by creating Address object and setting it's values
        @:return True if successful False otherwise"""
        add = Address(street=address, postcode=postcode)
        self.appointment.address.street = add.street
        self.appointment.address.postcode = add.postcode
        return self.appointment.address.street and self.appointment.address.postcode

    def __str__(self):
        """ String representation of Job."""
        try:
            specifics = "\n".join(f"{k}: {v}" for k, v in self.specific_reqs.items())
        except (TypeError, AttributeError):
            specifics = ""
        try:
            system_notes = "\n".join(f"{d:11.11} {a:5.5} {n:60.60}" for d, a, n in self.system_notes)
        except (TypeError, AttributeError):
            system_notes = ""
        try:
            notes = "\n".join(f"{n:100}" for n in self.notes)
        except (TypeError, AttributeError):
            notes = ""

        return \
            f"ID:\n{self.ref}\n" \
                f"CLIENT:\n{self.client}\n" \
                f"AGENT:\n{self.agent}\n" \
                f"VENDOR:\n{self.vendor}\n" \
                f"APPOINTMENT:\n{self.appointment}\n" \
                f"ADDRESS:\n{self.appointment.address}\n" \
                f"PROPERTY:\n{self.property_type}\n" \
                f"BEDS:\n{self.beds}\n" \
                f"FOLDER:\n{self.folder}\n" \
                f"NOTES:\n{notes}\n" \
                f"FLOORPLAN:\n{'Yes' if self.floorplan else 'No'}\n" \
                f"PHOTOS:\n{self.photos}\n" \
                f"SPECIFICS:\n{specifics}\n" \
                f"SYSTEM NOTES:\n{system_notes}"
