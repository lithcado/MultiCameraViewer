class CameraError(Exception):
    pass


class ParameterListError(CameraError):
    pass


class InitialError(CameraError):
    pass


class GetFrameError(CameraError):
    pass


class CameraReleaseError(CameraError):
    pass


class ParameterSetError(CameraError):
    pass


class FormatSetError(CameraError):
    pass

