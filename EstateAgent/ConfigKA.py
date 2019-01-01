from EstateAgent import pw

"""Configuration file containing complete specifications for accessing a client's webpage to enable
scraping of job related data
"""
# Environment variables-------------------------------------------------------------------------------------------------
CHROME_DRIVER =  "C:/Python36/selenium/webdriver/chrome/chromedriver.exe"  # '/usr/bin/chromedriver'# this should be the same for all configXX
#sdf


# -------------------------------------------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #
# --------------------------------------          LOG ON DATA                ----------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #

CLIENT = "KeyAGENT"
USERNAME = pw.USERNAME
PASSWORD = pw.PASSWORD
LOGIN_PAGE = "https://www.keyagent-portal.co.uk"
LANDING_PAGE = "https://www.keyagent-portal.co.uk/Site/Dea/home.aspx?Dea=272ca14b-8535-453f-bf30-10e5c0318651&TAB" \
               "=MYHOME"
USERNAME_FIELD = "ctl00$main$HipPlatformLogin$Username"
PASSWORD_FIELD = "ctl00$main$HipPlatformLogin$Password"
LOGIN_BUTTON = "ctl00$main$HipPlatformLogin$Button1"

# -------------------------------------------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #
# --------------------------------------              REGEXP                 ----------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #

REGEXP = {
        "JOB_PAGE_LINK": ".*Select.*",  # matches all links that point to job pages
        "AGENT":         r"(?:Agency Branch: )(.*)",  # matches Agent name after Agency Branch in notes.
        "VENDOR":        r"(?:)([ \w]*)(?: DAY)",  # matches Vendor name before DAY phone no.
        "PHONE_1":       r"(?:TEL:)(\D*\d{3,12}\D*\d{1,4}\D*\d{1,4})(?:\D*EVE)",  # matches Agent TEL phone no.
        "VENDOR_MOB":    r"(?:MOB:)(\D*\d{3,12}\D*\d{1,4}\D*\d{1,4})(?:\D*EVE)",  # matches Vendor MOB phone no.
        "AGENT_MOB":     r"(?:MOB:)(\D*\d{3,12}\D*\d{1,4}\D*\d{1,4})(?:\D*TEL)",  # matches Agent MOB phone number
        "PHONE_DAY":     r"(?:DAY:)(\D*\d{3,12}\D*\d{1,4}\D*\d{1,4})(?:\D*MOB)",  # matches Vendor DAY (main) phone no.
        "PHONE_EVE":     r"(?:EVE:)(\D*\d{3,12}\D*\d{1,4}\D*\d{1,4})(?:\D*Email)",  # matches Vendor EVE phone no.
        "PHOTO_COUNT":   r"(?:\D*)(\d+)\D*(?:photos)",  # matches number of photos required for job
}

# -------------------------------------------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #
# --------------------------------------        HTML ID TAGS FOR DATA        ----------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #

# for data stored in html tags {name:html tag ref}
JOB_PAGE_DATA = {
        "JOB_DATA_AGENT":               "ctl00_main_LabelAgent",
        "JOB_DATA_VENDOR":              "ctl00_main_LabelVendor",
        "JOB_DATA_FLOORPLAN":           "ctl00_main_LabelRequiresFloorplan",
        "JOB_DATA_PHOTOS":              "ctl00_main_LabelRequiresPhotos",
        "JOB_DATA_PROPERTY_TYPE":       "ctl00_main_LabelPropertyType",
        "JOB_DATA_BEDS":                "ctl00_main_LabelNumberBeds",
        "JOB_DATA_NOTES":               "ctl00_main_textBoxCaseNotes",
        "JOB_DATA_BRANCH_NOTES":        "ctl00_main_TextBoxBranchnote",
        "JOB_DATA_SENT":                "ctl00_main_LabelInviteSent",
        "JOB_DATA_CONFIRMED":           "ctl00_main_LabelConfirmedDate",
        "JOB_DATA_APPOINTMENT":         "ctl00_main_LabelAppointment",
        "JOB_DATA_APPOINTMENT_ADDRESS": "ctl00_text_LabelAddress",
        "JOB_DATA_ID":                  "ctl00_text_LabelHipref"
}
# for data stored in html tables {name: html table ref}
JOB_PAGE_TABLES = {
        "JOB_DATA_SPECIFIC_REQS_TABLE": "ctl00_main_GridViewPhotoLocation",
        "JOB_DATA_HISTORY_TABLE":       "ctl00_main_GridViewTaskNotes"
}

# -------------------------------------------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #
# --------------------------------------          HTML BUTTONS               ----------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #

JOB_PAGE_BUTTONS = {
        "JOB_DECLINE":           "ctl00_main_ButtonDecline",
        "JOB_ADD_NOTE":          "ctl00_main_ButtonAddNoteAppointment",
        "JOB_SAVE_APPT":         "ctl00_main_ButtonSaveAppointment",
        "JOB_SAVE_NO_APPT":      "ctl00_main_ButtonSaveNoAppointment",
        "JOB_CHANGE_APPT":       "ctl00_main_ButtonChangeAppointment",
        "JOB_NO_APPT_DROPDOWN":  "ctl00_main_DropDownListNoAppointment",
        "JOB_DATE_ENTRY":        "ctl00_main_TextBoxAppointmentDate",
        "JOB_TIME_ENTRY":        "ctl00_main_TextBoxAppointmentTime",
        "JOB_FAST_UPLOAD":       "ctl00_main_ButtonFastUpload",
        "JOB_CONFIRM_FLOORPLAN": "ctl00_main_ConfirmFloorplanUpload",
        "JOB_CONFIRM_PHOTOS":    "ctl00_main_ConfirmPhotoUpload",
        "JOB_BACK":              "ctl00_main_ButtonBack"
}
UPLOAD_PAGE_BUTTONS = {
        "UPLOAD_SELECT_FLOORPLAN": "fileFloorplans",
        "UPLOAD_UPLOAD_FLOORPLAN": "ancFloorplans",
        "UPLOAD_SELECT_PHOTOS":    "filePhotos",
        "UPLOAD_UPLOAD_PHOTOS":    "ancPhotos",
        "UPLOAD_CLOSE":            "ButtonClose",
}

# -------------------------------------------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #
# --------------------------------------          CLIENT SPECIFIC            ----------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #
TIME_FORMAT = "%a-%d %b %y %H%M"
UNWANTED_NOTES = [": NA", "Sample Selector:", "Agency Branch:", "AA Prestige"]
JOB_PAGE_SITE_VISIT_ABBRS = {
        "Appointment date ammended":      "Changed ",
        "Appointment":                    "appt",
        "Steve Caballero":                "SC",
        " due to the reason":             ":",
        "The Supplier has confirmed the": "Confirmed",
        "Floorplan":                      "FP",
        "(DEA)":                          "",
        "please explain":                 "",
        "Added by the Supplier:":         "",
        "I will call again":              " will try again",
        "Changed at Vendors request":     ""
}
CHANGE_APPT_BUTTONS = {
        "CHANGE_SELECT":         "ctl00_main_DropDownListAppointmentChangedReasons",
        "CHANGE_SELECT_OPTIONS": {
                "AGENT_REQ":     "Changed at Agents request",
                "VENDOR_REQ":    "Changed at Vendors request",
                "NO_ACCESS":     "Attended property, no access",
                "WEATHER":       "Change due to weather",
                "DOUBLE_BOOKED": "Double booked", "OTHER": "I was unable to attend because",
        },
        "CHANGE_TEXT_BOX":       "ctl00_main_textboxAppointmentChangeReason",
        "CHANGE_APPT_DATE":"ctl00_main_txtNewChangedAppointmentDate",
        "CHANGE_APPT_TIME":"ctl00_main_txtNewChangedAppointmentTime",
        "CHANGE_SAVE":"ctl00_main_ButtonShareAppointmentChange",
        "CHANGE_CANCEL":"ctl00_main_ButtonCancelAppointmentChange"
}
