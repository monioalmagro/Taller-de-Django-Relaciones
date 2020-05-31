from django.db import models

class Producto(models.Model):
    titulo = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.titulo

class Carrito(models.Model):
    productos = models.ManyToManyField(Producto, through='CarritoProducto')
  
# Many genera nueva tabla carrito_id y producto_id #llaves foraneas

    """ def __str__(self):
        return self.productos """

class CarritoProducto(models.Model):
    carrito_id = models.ForeignKey(Carrito,on_delete=models.CASCADE)
    producto_id = models.ForeignKey(Producto,on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)


  