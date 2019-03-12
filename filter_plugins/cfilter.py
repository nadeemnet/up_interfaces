class FilterModule(object):

    def count_all_eth_interfaces(self, if_list):
        interface_list = []
        for k, v in if_list.items():
            for k1, v1 in v.items():
                if 'Ethernet' in k1:
                    interface_list.append(k1)
        return len(interface_list)

    def count_all_up_interfaces(self, if_list):
        count = 0
        for k, v in if_list.items():
            for k1, v1 in v.items():
                if 'Ethernet' in k1:
                    if v1['is_up']:
                        count += 1
        return count

    def filters(self):
        return {'count_eth': self.count_all_eth_interfaces, 'count_up': self.count_all_up_interfaces}
