from .models import ArtisticIp as ArtisticIpModel


class ArtYp(object):
    """docstring for ArtYp."""

    def __init__(self, arg):
        super(ArtYp, self).__init__()
        self.arg = arg

    @staticmethod
    def get_ip_with_django(**kwargs):
        try:
            request = kwargs.pop('request')
        except Exception as e:
            print('[ArtYp] get_ip_with_django(request=request)')
            print('[ArtYp] filepath : {0}'.format(__file__))
            raise

        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')

        print('[ArtYp] IP entrant : {0}'.format(ip))

        return ip


    @staticmethod
    def save_ip(ipv4):

        if len(ipv4.split('.')) != 4:
            ipv6 = ipv4.split(':')
            if len(ipv6 > 2):
                ipv4 = '777.{0}.{1}.{2}'.format(ipv6[0], ipv6[1], ipv6[2])
            else:
                ipv4 = '333.444.444.333'

        lay_a, lay_b, lay_c, lay_d = ipv4.split('.')

        artistic_ip = ArtisticIpModel.objects.filter(lay_a=lay_a, lay_b=lay_b, lay_c=lay_c, lay_d=lay_d).first()

        if artistic_ip is None:
            artistic_ip = ArtisticIpModel.objects.create(lay_a=lay_a, lay_b=lay_b, lay_c=lay_c, lay_d=lay_d)

        pass

    @staticmethod
    def get_ip_tree():

        ip_tree = {}

        # lay_value = {
        #   'type': 'a',
        #        'value': ipv4.lay_a,
        #        'children': {},
        # }
        # ip_tree['lay_value'] = lay_value

        artistic_ip_all = ArtisticIpModel.objects.all()

        for ipv4 in artistic_ip_all:

            # Si la racine n'existe pas, la fonction la crée.
            lay_a_name = 'lay_{0}'.format(ipv4.lay_a)
            ip_tree_lay_a_keys = ip_tree.keys()
            if lay_a_name not in ip_tree_lay_a_keys:
                lay_a = {
                    'type': 'a',
                    'value': ipv4.lay_a,
                    'children': {},
                }

                ip_tree[lay_a_name] = lay_a
            # Sinon, on continue

            # Si l'étage B n'existe pas, la fonction la crée.
            lay_b_name = 'lay_{0}'.format(ipv4.lay_b)
            ip_tree_lay_b_keys = ip_tree[lay_a_name]['children'].keys()
            if lay_b_name not in ip_tree_lay_b_keys:
                lay_b = {
                    'type': 'b',
                    'value': ipv4.lay_b,
                    'children': {},
                }

                ip_tree[lay_a_name]['children'][lay_b_name] = lay_b


            # Si l'étage B n'existe pas, la fonction la crée.
            lay_c_name = 'lay_{0}'.format(ipv4.lay_c)
            ip_tree_lay_c_keys = ip_tree[lay_a_name]['children'][lay_b_name]['children'].keys()
            if lay_c_name not in ip_tree_lay_c_keys:
                lay_c = {
                    'type': 'c',
                    'value': ipv4.lay_c,
                    'children': {},
                }

                ip_tree[lay_a_name]['children'][lay_b_name]['children'][lay_c_name] = lay_c


            # Si l'étage B n'existe pas, la fonction la crée.
            lay_d_name = 'lay_{0}'.format(ipv4.lay_d)
            ip_tree_lay_d_keys = ip_tree[lay_a_name]['children'][lay_b_name]['children'][lay_c_name]['children'].keys()
            if lay_d_name not in ip_tree_lay_d_keys:
                lay_d = {
                    'type': 'd',
                    'value': ipv4.lay_d,
                    'deploy': ipv4,
                }

                ip_tree[lay_a_name]['children'][lay_b_name]['children'][lay_c_name]['children'][lay_d_name] = lay_d

        return ip_tree

    @staticmethod
    def ip_tree_to_list(ip_tree):

        list = []

        for lay_a in ip_tree.values():
            for lay_b in lay_a['children'].values():
                for lay_c in lay_b['children'].values():
                    for lay_d in lay_c['children'].values():
                        list.append(lay_d['deploy'])

        return list
