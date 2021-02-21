class SwimmingPoll:
    number_of_swimmers_per_trainer = 8
    def __init__(self, address = '', capacity = 0, max_visitors_per_time = 0, length = 25, width= 10, depth = 3):
        self.address= address
        self.capacity= capacity
        self.max_visitors_per_time= max_visitors_per_time
        self.width = width
        self.length = length
        self.depth = depth

    def __del__(self):
        print('Finished,destructor worked\n')

    def __str__(self):
       return "Address: {} \t CapacityOfWaterInLiters: {}\t MaxVisitors: {}".format(self.address, self.capacity, self.max_visitors_per_time)

    @staticmethod
    def get_allowed_number_of_swimmers_per_trainer():
        return SwimmingPoll.number_of_swimmers_per_trainer


def main (*args):
    array_of_str = []
    array_of_int = []
    for i in args:
        if isinstance(i, str):
            array_of_str.append(i)
        elif isinstance(i, int):
            array_of_int.append(i)
    array_of_objects = []
    counter_of_input_int = 0
    counter_of_input_str = 0
    for counter_of_objects in range(3):
        if counter_of_input_str >= len(array_of_str):
            array_of_str.append('Default')
        if counter_of_input_int >= len(array_of_int):
                array_of_int.append(0)
        if (counter_of_input_int+1)>= len(array_of_int):
               array_of_int.append(0)
        array_of_objects.append(SwimmingPoll(array_of_str[counter_of_input_str],array_of_int[counter_of_input_int],array_of_int[counter_of_input_int+1]))
        counter_of_input_str += 1
        counter_of_input_int += 2
        print(array_of_objects[counter_of_objects])


if __name__ == '__main__':
    main('aaa',155,25,377,'bbb',66,67,77,555)
    print('Allowed number of swimmers for training by one trainer :',SwimmingPoll.get_allowed_number_of_swimmers_per_trainer())