from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# PUBLIC_INTERFACE
@api_view(['GET'])
def health(request):
    """Health check endpoint. Returns server status."""
    return Response({"message": "Server is up!"})

# PUBLIC_INTERFACE
@api_view(['GET', 'POST'])
def add(request):
    """
    Add two numbers together.

    Accepts:
        - GET: query parameters 'a' and 'b'
        - POST: JSON body {"a": <number>, "b": <number>}

    Returns:
        JSON: { "result": <result> }
    """
    a, b, error = _get_inputs(request)
    if error:
        return Response({"error": error}, status=status.HTTP_400_BAD_REQUEST)
    return Response({"result": a + b})

# PUBLIC_INTERFACE
@api_view(['GET', 'POST'])
def subtract(request):
    """
    Subtract b from a.

    Accepts:
        - GET: query parameters 'a' and 'b'
        - POST: JSON body {"a": <number>, "b": <number>}

    Returns:
        JSON: { "result": <result> }
    """
    a, b, error = _get_inputs(request)
    if error:
        return Response({"error": error}, status=status.HTTP_400_BAD_REQUEST)
    return Response({"result": a - b})

# PUBLIC_INTERFACE
@api_view(['GET', 'POST'])
def multiply(request):
    """
    Multiply two numbers.

    Accepts:
        - GET: query parameters 'a' and 'b'
        - POST: JSON body {"a": <number>, "b": <number>}

    Returns:
        JSON: { "result": <result> }
    """
    a, b, error = _get_inputs(request)
    if error:
        return Response({"error": error}, status=status.HTTP_400_BAD_REQUEST)
    return Response({"result": a * b})

# PUBLIC_INTERFACE
@api_view(['GET', 'POST'])
def divide(request):
    """
    Divide a by b.

    Accepts:
        - GET: query parameters 'a' and 'b'
        - POST: JSON body {"a": <number>, "b": <number>}

    Returns:
        JSON: { "result": <result> }
        Returns HTTP 400 if b == 0.
    """
    a, b, error = _get_inputs(request)
    if error:
        return Response({"error": error}, status=status.HTTP_400_BAD_REQUEST)
    if b == 0:
        return Response({"error": "Division by zero is not allowed."}, status=status.HTTP_400_BAD_REQUEST)
    return Response({"result": a / b})

def _get_inputs(request):
    """
    Helper to extract two numbers (a and b) from GET query params or JSON body.
    Returns: (a, b, None) if correct, or (None, None, error_msg) if error.
    """
    try:
        if request.method == 'GET':
            a = request.query_params.get('a')
            b = request.query_params.get('b')
        else:
            a = request.data.get('a')
            b = request.data.get('b')
        if a is None or b is None:
            return None, None, "Both parameters 'a' and 'b' are required."
        a = float(a)
        b = float(b)
        return a, b, None
    except (ValueError, TypeError):
        return None, None, "Parameters 'a' and 'b' must be numbers."
