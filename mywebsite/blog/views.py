from django.shortcuts import redirect, render
from .models import Buku
from .form import FormBuku
from django.contrib import messages
# Create your views here.

def ubah_buku(request, id_buku):
    buku = Buku.objects.get(id=id_buku)
    template = 'ubah-buku.html'
    if request.POST:
        form = FormBuku(request.POST, instance=buku)
        if form.is_valid():
            form.save()
            messages.success(request, "Data Berhasil diubah")
            return redirect('b', id_buku=id_buku)
    else:
        form =FormBuku(instance=buku)
        konteks = {
            'form' : form,
            'buku' : buku,
        }
    return render(request, template, konteks)
    
def buku(request):
    books = Buku.objects.all()
    konteks = {
        'books' : books,
    }
    return render(request,'buku.html', konteks)

# def create(request):
#     post_form = PostForm(request.Buku or None)
#     if request.method == 'POST':
#         if post_form.is_valid():
#             Buku.objects.create(
#                 judul = request.POST.get('judul'),
#                 penulis = request.POST.get('penulis'),
#                 penerbit = request.POST.get('penerbit'),
#                 jumlah_buku = request.POST.get('jumlah_buku'),
#             )

#             return redirect('blog:buku')
#     context = {
#         'post_title' : 'create post',
#         'post_form' : post_form,
#     }
#     return render(request,'create.html',context)

def tambah_buku(request):
    if request.POST:
        form = FormBuku(request.POST)
        if form.is_valid():
            form.save()
            form = FormBuku()
            pesan = "Data Berhasil Disimpan"
            konteks = {
                'form' : form,
                'pesan' : pesan,
            }
            return render(request,'tambah-buku.html',konteks)
    else:
        form = FormBuku()

    konteks = {
        'form' : form,
    }

    return render(request,'tambah-buku.html',konteks)


def hapus_buku(request, id_buku):
    buku = Buku.objects.filter(id=id_buku)
    buku.delete()

    return redirect('buku')