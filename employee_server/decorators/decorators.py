from rest_framework.response import Response
from rest_framework.views import status


def validate_request_data(foo):
    def decorated(*args, **kwargs):
        last_name=args[0].request.data.get("last_name", ""),
        first_name=args[0].request.data.get("first_name", ""),
        middle_name=args[0].request.data.get("middle_name", ""),
        position=args[0].request.data.get("position", ""),
        employment_date=args[0].request.data.get("employment_date", ""),
        salary=args[0].request.data.get("salary", ""),
        chief=args[0].request.data.get("chief", ""),
        unit=args[0].request.data.get("unit", ""),
        photo=args[0].request.data.get("photo", ""),
        email=args[0].request.data.get("email", ""),
        if not last_name and not first_name and not middle_name and not position and not employment_date and not salary and not chief and not unit and not photo and not email:
            return Response(
                data={
                    "message": "required to add a unit"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        return foo(*args, **kwargs)
    return decorated