from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


from .models import Category,Product,ProductGallery
from .serializers import CategorySerializer,ProductSerializer,ProductGallerySerializer

@api_view(['POST'])
@permission_classes([IsAdminUser])
def createCategory(request):
    data = request.data
    try:
        
        category = Category.objects.create(
        category_name=data['category_name'],
        slug=data['slug'],
        description=data['description'],
        )
        serializer = CategorySerializer(category, many=False)
        return Response(serializer.data)
    except:
        message = {'detail': 'Category already exists'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def getCategories(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getProducts(request):
    # print(request.GET['search'])
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def singleProduct(request,pk):
    product = Product.objects.get(id=pk)
    serializer = ProductSerializer(product, many=False)
    image = ProductGallery.objects.filter(product=product)
    serializeImage = ProductGallerySerializer(image, many=True)
    data = {
        'product': serializer.data,
        'image': serializeImage.data
    }
    return Response(data)

@api_view(['GET'])
def filterProducts(request):
    category = request.GET.get('category')
    search = request.GET.get('search')
    if search == None:
        search = ''
    products = Product.objects.filter(product_name__icontains=search,category__category_name__icontains=category)
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)