from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Produit
from .serializers import ProduitSerializer

@api_view(['GET'])
def api_product_list(request):
    produits = Produit.objects.all()
    serializer = ProduitSerializer(produits, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def api_product_detail(request, pk):
    try:
        produit = Produit.objects.get(pk=pk)
    except Produit.DoesNotExist:
        return Response({'error': 'Produit non trouvé'}, status=404)
    
    serializer = ProduitSerializer(produit)
    return Response(serializer.data)

@api_view(['POST'])
def api_product_create(request):
    serializer = ProduitSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['PUT', 'PATCH'])
def api_product_update(request, pk):
    try:
        produit = Produit.objects.get(pk=pk)
    except Produit.DoesNotExist:
        return Response({'error': 'Produit non trouvé'}, status=404)

    serializer = ProduitSerializer(produit, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
def api_product_delete(request, pk):
    try:
        produit = Produit.objects.get(pk=pk)
    except Produit.DoesNotExist:
        return Response({'error': 'Produit non trouvé'}, status=404)

    produit.delete()
    return Response({'message': 'Produit supprimé avec succès'}, status=204)
