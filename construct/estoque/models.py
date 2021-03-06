from django.db import models

# Create your models here.

class Categoria(models.Model):
    titulo =  models.CharField('titulo', max_length=40)
    created_at = models.DateTimeField('criado em', auto_now=True)
    
    class Meta: 
        verbose_name_plural = 'estoques'
        verbose_name = 'estoque'
        ordering = ('-created_at',)

    def __str__(self):
        return self.titulo   

class Produto(models.Model):
    nome =  models.CharField('produto', max_length=40)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True,verbose_name='categoria',)
    quantidade = models.FloatField('quantidade', )
    preco_compra = models.FloatField('preço de compra', )
    preco_venda = models.FloatField('preço de venda', )

    def gerar_desconto(self, desconto):
        #self.preco_venda - ((self.preco_venda * desconto)/100)
        return (self.preco_venda * (desconto-100))

    def lucro(self):
        lucro = self.preco_venda - self.preco_compra
        return (lucro * 100) / self.preco_compra

    class Meta: 
        verbose_name_plural = 'produtos'
        verbose_name = 'produto'
        ordering = ('-quantidade',)

    def __str__(self):
        return self.nome   

    