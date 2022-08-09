
import json
from django.shortcuts import redirect, render
from core.models import endereco
import requests as requests
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages


def index(request):

    return render(request, 'index.html')

def buscar_cep(request):

    try:
        if request.method=='POST':
            cep =  request.POST.get('cep')
            cep= str(cep)
            endereço = endereco.objects.get(cep=cep)

            logradouro = endereço.logradouro
            bairro = endereço.bairro
            cidade = endereço.cidade_estado

            resposta= requests.get(f'https://viacep.com.br/ws/{cep}/json/')
            var= resposta.text

            messages.success(
                request,
                'Cep consultado com sucesso !!!'
            )
            context = {'logradouro':logradouro,
                        'bairro':bairro,
                        'cidade':cidade,
                        'var' : var,
            }

            return render(request, 'index.html',context)

            

        #Se o Cep nao constar na base de dados, esse except será executado
    except ObjectDoesNotExist:

        cep =  request.POST.get('cep')
        cep= str(cep)
        resposta= requests.get(f'https://viacep.com.br/ws/{cep}/json/')
        
        var = resposta.text
        convertido = json.loads(var)

        cep_sem_hifen= cep

        localidade = endereco.objects.create(cep=cep_sem_hifen, logradouro=convertido['logradouro'], bairro=convertido['bairro'], cidade_estado=convertido['localidade'])
        localidade.save()
        
        messages.success(
                request,
                'O cep consultado não existia na base de dados, mas agora foi inserido apartir do JSON abaixo, busque novamente !!!'
            )

        context = {
                    'convertido' : convertido,
        }


        print('seu cep esta na nossa base de dados agora ')
    return render(request, 'index.html',context)

