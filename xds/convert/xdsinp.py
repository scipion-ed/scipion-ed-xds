"""Template for XDS input files"""


def readInputImages(inputImages):
    """ Function to get all the relevant parameters from a set of diffraction images """
    imageList = [img.clone() for img in inputImages]
    firstimage = imageList[0]
    lastimage = imageList[-1]
    parameters = {}
    parameters['NameTemplate'] = "{}/0????.img".format(firstimage.getDirName())
    parameters['ImageRange'] = [firstimage.getIndex(), lastimage.getIndex()]
    return parameters


def writeTemplate(inputImages, outputpath=None, **kwargs):
    from datetime import datetime
    params = readInputImages(inputImages)
    now = datetime.now()
    dt_string = now.strftime("%a %b %-d %H:%M:%S %Y")

    template = ("""! XDS.INP file for Rotation Electron Diffraction generated by `scipion-ed-xds`
    ! Fri May  3 12:11:17 2019
    ! {}
    ! For definitions of input parameters, see:
    ! http://xds.mpimf-heidelberg.mpg.de/html_doc/xds_parameters.html
    !
    ! cRED implementation reference paper:
    ! J. Appl. Cryst. (2018). 51, 1652–1661. http://dx.doi.org/10.1107/S1600576718015145

    ! ********** Job control **********

    !JOB= XYCORR INIT COLSPOT IDXREF
    !JOB= DEFPIX INTEGRATE CORRECT
    !JOB= CORRECT
    JOB= COLSPOT


    MAXIMUM_NUMBER_OF_JOBS=4
    MAXIMUM_NUMBER_OF_PROCESSORS=4

    ! ********** Data images **********

    NAME_TEMPLATE_OF_DATA_FRAMES= {}   SMV
    DATA_RANGE=           {} {}
    SPOT_RANGE=           {} {}
    BACKGROUND_RANGE=     {} {}
    EXCLUDE_DATA_RANGE=10 10
    EXCLUDE_DATA_RANGE=20 20
    EXCLUDE_DATA_RANGE=30 30
    EXCLUDE_DATA_RANGE=40 40
    EXCLUDE_DATA_RANGE=50 50
    EXCLUDE_DATA_RANGE=60 60
    EXCLUDE_DATA_RANGE=70 70
    EXCLUDE_DATA_RANGE=80 80
    EXCLUDE_DATA_RANGE=90 90
    EXCLUDE_DATA_RANGE=100 100
    EXCLUDE_DATA_RANGE=110 110
    EXCLUDE_DATA_RANGE=120 120
    EXCLUDE_DATA_RANGE=130 130
    EXCLUDE_DATA_RANGE=140 140
    EXCLUDE_DATA_RANGE=150 150
    EXCLUDE_DATA_RANGE=160 160

    ! ********** Crystal **********

    !SPACE_GROUP_NUMBER= 0
    !UNIT_CELL_CONSTANTS= 10 20 30 90 90 90

    !REIDX=                       !Optional reindexing transformation to apply on reflection indices
    FRIEDEL'S_LAW=TRUE            !TRUE is default

    !phi(i) = STARTING_ANGLE + OSCILLATION_RANGE * (i - STARTING_FRAME)
    STARTING_ANGLE= -33.9000
    STARTING_FRAME= 1

    MAX_CELL_AXIS_ERROR=  0.05      !0.03 is default
    MAX_CELL_ANGLE_ERROR= 3.0       !2.0  is default

    TEST_RESOLUTION_RANGE=10. 1.0 !for calculation of Rmeas when analysing the intensity data for space group symmetry in the CORRECT step.
    !MIN_RFL_Rmeas=50             !50 is default - used in the CORRECT step for identification of possible space groups.
    !MAX_FAC_Rmeas=2.0            !2.0 is default - used in the CORRECT step for identification of possible space groups.

    ! ********** Detector hardware **********

    NX=516     NY=516             !Number of pixels
    QX=0.0550  QY=0.0550          !Physical size of pixels (mm)
    OVERLOAD= 130000              !default value dependent on the detector used
    TRUSTED_REGION= 0.0  1.05   !default "0.0 1.05". Corners for square detector max "0.0 1.4142"

    DETECTOR= PILATUS      ! Pretend to be PILATUS detector to enable geometric corrections
    X-GEO_CORR= XCORR.cbf  ! X stretch correction
    Y-GEO_CORR= YCORR.cbf  ! Y stretch correction

    SENSOR_THICKNESS=0.30
    AIR=0.0

    ! ********** Trusted detector region **********

    !Mark cross as untrusted region
    UNTRUSTED_RECTANGLE= 255 262 0 517
    UNTRUSTED_RECTANGLE= 0 517 255 262

    VALUE_RANGE_FOR_TRUSTED_DETECTOR_PIXELS= 10 30000 !Values are defined in `ABS.CBF`, check mask in `BKGPIX.CBF`, used in DEFPIX
    !MINIMUM_ZETA=                                    !0.05 is default

    INCLUDE_RESOLUTION_RANGE= 20 0.8

    !Ice Ring exclusion, important for data collected using cryo holders
    !EXCLUDE_RESOLUTION_RANGE= 3.93 3.87       !ice-ring at 3.897 Angstrom
    !EXCLUDE_RESOLUTION_RANGE= 3.70 3.64       !ice-ring at 3.669 Angstrom
    !EXCLUDE_RESOLUTION_RANGE= 3.47 3.41       !ice-ring at 3.441 Angstrom (Main)
    !EXCLUDE_RESOLUTION_RANGE= 2.70 2.64       !ice-ring at 2.671 Angstrom
    !EXCLUDE_RESOLUTION_RANGE= 2.28 2.22       !ice-ring at 2.249 Angstrom (Main)
    !EXCLUDE_RESOLUTION_RANGE= 2.102 2.042     !ice-ring at 2.072 Angstrom - strong
    !EXCLUDE_RESOLUTION_RANGE= 1.978 1.918     !ice-ring at 1.948 Angstrom - weak
    !EXCLUDE_RESOLUTION_RANGE= 1.948 1.888     !ice-ring at 1.918 Angstrom - strong
    !EXCLUDE_RESOLUTION_RANGE= 1.913 1.853     !ice-ring at 1.883 Angstrom - weak
    !EXCLUDE_RESOLUTION_RANGE= 1.751 1.691     !ice-ring at 1.721 Angstrom - weak

    ! ********** Detector geometry & Rotation axis **********

    DIRECTION_OF_DETECTOR_X-AXIS= 1 0 0
    DIRECTION_OF_DETECTOR_Y-AXIS= 0 1 0

    ORGX= 219.70    ORGY= 226.65           !Detector origin (pixels). Often close to the image center, i.e. ORGX=NX/2; ORGY=NY/2
    DETECTOR_DISTANCE= +532.28            !Can be negative. Positive because the detector normal points away from the crystal.

    OSCILLATION_RANGE= 0.3512
    !OSCILLATION_RANGE 0.3515               !Calibrated value if above one is too far off

    ROTATION_AXIS= -0.6204 0.7843 0.0000

    ! ********** Incident beam **********

    X-RAY_WAVELENGTH= 0.0251              !used by IDXREF
    INCIDENT_BEAM_DIRECTION= 0 0 1        !The vector points from the source towards the crystal

    ! ********** Background and peak pixels **********

    !NBX=7  NBY=7            ! 3 is default, used to estimate the expected variation in a data image, see GAIN.cbf
    !BACKGROUND_PIXEL= 6.0   ! Background pixel belongs to background if variation less than given esds
    !STRONG_PIXEL= 3.0       ! Strong pixel must exceed background by more than number of given esds
    !MAXIMUM_NUMBER_OF_STRONG_PIXELS= 1500000 ! Approximate upper limit for the total number of 'strong' pixels
    !MINIMUM_NUMBER_OF_PIXELS_IN_A_SPOT= 6    ! Used to suppress spurious, isolated 'strong' pixels from entering the spot list
    !SPOT_MAXIMUM-CENTROID= 3.0               ! Maximum deviation of spot maximum from spot centroid
    !SIGNAL_PIXEL= 3.0                        ! Signal pixels must exceed background by more than given esds

    ! ********** Refinement **********

     REFINE(IDXREF)=    BEAM AXIS ORIENTATION CELL !POSITION
     REFINE(INTEGRATE)= !POSITION BEAM AXIS !ORIENTATION CELL
     REFINE(CORRECT)=   BEAM AXIS ORIENTATION CELL !POSITION

    ! ********** Indexing **********

    MINIMUM_FRACTION_OF_INDEXED_SPOTS= 0.25    !0.50 is default.

    """.format(dt_string,
               params.get("NameTemplate"),
               params.get("ImageRange")[0],
               params.get("ImageRange")[1],
               params.get("ImageRange")[0],
               params.get("ImageRange")[1],
               params.get("ImageRange")[0],
               params.get("ImageRange")[1]
               ))
    with open("XDS.INP", "w") as text_file:
        print("{}".format(template), file=text_file)
