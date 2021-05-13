from django.shortcuts import render

from .artyp import ArtYp

# Create your views here.
def home(request):

    artistic_tab = []

    def generate_lays_a_b_in(tab):
        for i in range(256):
            print("Loop {0}".format(i))
            tab.append([])
            for j in range(256):
                tab[i].append([i, j])
    #            for k in range(256):
    #                tab[i][j].append([i, j, k])
    #                for l in range(256):
    #                    tab[i][j][k].append([i, j, k, l])

    ArtYp.save_ip(ArtYp.get_ip_with_django(request=request))

    ip_tree = ArtYp.get_ip_tree()
    artistic_list = ArtYp.ip_tree_to_list(ip_tree)

    context = {
        'artistic_list': artistic_list,
    }

    return render(request, 'greentea/home.html', context)
