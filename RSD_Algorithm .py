from pprint import pprint
# ---------------------------------------------------------------------------- #
# samples                                                                      #
# ---------------------------------------------------------------------------- #


# agents = {
#         0 : [6, 3, 2, 5, 1, 7, 4, 0],
#         1 : [6, 3, 1, 2, 5, 7, 0, 4],
#         2 : [6, 0, 2, 1, 0, 7, 5, 4],
#         3 : [6, 0, 1, 3, 2, 7, 4, 5],
#         4 : [6, 5, 2, 0, 4, 7, 3, 1],
#         5 : [6, 5, 2, 1, 4, 7, 3, 0],
#         6 : [6, 5, 2, 1, 4, 7, 3, 0],
#         7 : [6, 5, 2, 1, 4, 7, 3, 0],
#     }

# agents = {
#     0 : [6, 3, 2, 5, 1, 4, 0],
#     1 : [6, 3, 1, 2, 5, 0, 4],
#     2 : [6, 0, 2, 1, 0, 5, 4],
#     3 : [6, 0, 1, 3, 2, 4, 5],
#     4 : [6, 5, 2, 0, 4, 3, 1],
#     5 : [6, 5, 2, 1, 4, 3, 0],
#     6 : [6, 5, 2, 1, 4, 3, 0],
#}

# agents = {
#         0 : [3, 2, 5, 1, 4, 0],
#         1 : [3, 1, 2, 5, 0, 4],
#         2 : [0, 2, 1, 0, 5, 4],
#         3 : [0, 1, 3, 2, 4, 5],
#         4 : [5, 2, 0, 4, 3, 1],
#         5 : [5, 2, 1, 4, 3, 0],
#     }

# agents = {
#         0 : [3, 2, 1, 4, 0],
#         1 : [3, 1, 2, 0, 4],
#         2 : [0, 2, 1, 0, 4],
#         3 : [0, 1, 3, 2, 4],
#         4 : [2, 0, 4, 3, 1],
#     }

agents = {
    0: [0, 1, 2, 3],
    1: [0, 1, 2, 3],
    2: [2, 0, 1, 3],
    3: [2, 3, 0, 1],
}

# agents = {
#         0 : [0, 1, 2],
#         1 : [0, 1, 2],
#         2 : [1, 2, 0],
#     }

# agents = {
#     0 : [1, 0],
#     1 : [1, 0],
#}

# --------------------------------------------------------------------------- #


# ------------------------------ #
#    for more pretty printing:   #
# ------------------------------ #
def pretty(d, indent=0):
   for key, value in d.items():
      print('\t' * indent + str(key))
      if isinstance(value, dict):
         pretty(value, indent+1)
      else:
         print('\t' * (indent+1) + str(value))
# ---------------------------------------------------------------------------- #


def set_order_of_agents_items(agents_param, sorted_agents_param, current_order_param):
    global growth_RSD_items, last_RSD_item_number
    for agent_key in agents_param:
        order = current_order_param
        # ------------------------------------------------------- #
        #    for each new allocating item, clear last sorted agent:   #
        # ------------------------------------------------------- #
        sorted_agents_param[order] = {}
        if len(agents_param) > 1:
            sorted_agents_param[order][agent_key] = agents_param[agent_key]
            # --------------------------------------------------------- #
            #    clear current sorted agent for next sorting step(s):   #
            # --------------------------------------------------------- #
            result_of_current_step = agents_param.copy()
            del result_of_current_step[agent_key]
            next_order = order + 1
            set_order_of_agents_items(result_of_current_step, sorted_agents_param, next_order)
        # --------------------------------------------------------- #
        #    sorting part for last agent in current sorting item:   #
        # --------------------------------------------------------- #
        elif len(agents_param) == 1:
            # --------------------------------------------- #
            #    sort last agent in current sorting item:   #
            # --------------------------------------------- #
            sorted_agents_param[order][agent_key] = agents_param[agent_key].copy()
            # --------------------------------- #
            #    store current sorting item :   #
            # --------------------------------- #
            growth_RSD_items[last_RSD_item_number] = sorted_agents_param.copy()
            # ----------------------------------------------------- #
            #    prepare the key for store the next sorting item:   #
            # ----------------------------------------------------- #
            last_RSD_item_number += 1
# ---------------------------------------------------------------------------- #


def set_various_allocates(growth_RSD_items_param, goods_list_param):
    global random_allocated_matrices, number_of_growth_RSD_items
    # ------------------------------------------------------ #
    #    here, number of allocated matrices begins from 0:   #
    # ------------------------------------------------------ #
    index_of_allocated_matrix = 0
    for index_of_item in growth_RSD_items_param:
        random_allocated_matrices[index_of_allocated_matrix] = {}
        goods_list_for_each_steps = goods_list_param.copy()
        for order in growth_RSD_items_param[index_of_item]:
            agent = growth_RSD_items_param[index_of_item][order]
            # -------------------------------------------- #
            #    getting key(agent index) of each agent:   #
            # -------------------------------------------- #
            agent_key = list(agent.keys())[0]
            random_allocated_matrices[index_of_allocated_matrix][agent_key] = {}
            # ----------------------------------------------- #
            #    here, agents tendency index begins from 0:   #
            # ----------------------------------------------- #
            best_remained_good_index_for_agent = 0
            if len(goods_list_for_each_steps) > 1:
                if agent[agent_key][best_remained_good_index_for_agent] in goods_list_for_each_steps:
                    # ----------------------------------------------------------- #
                    #    set the definitive allocating matrix for current agent   #
                    # ----------------------------------------------------------- #
                    for i in range(len(goods_list_param)):
                        if i == agent[agent_key][best_remained_good_index_for_agent]:
                            # ------------------------------------------------------- #
                            #    if current good(index) allocated to current agent:   #
                            # ------------------------------------------------------- #
                            random_allocated_matrices[index_of_allocated_matrix][agent_key][i] = 1
                            del goods_list_for_each_steps[i]
                        else:
                            random_allocated_matrices[index_of_allocated_matrix][agent_key][i] = 0
                else:
                    # -------------------------------------------------------------------------------------------------------------------------- #
                    #    if first best good for current agent does not available, now best_remained_good_index_for_agent+1, becomes equal to 1:  #
                    # -------------------------------------------------------------------------------------------------------------------------- #
                    for i in range(1, len(goods_list_param), 1):
                        if (agent[agent_key][i] in goods_list_for_each_steps):
                            # ----------------------------------------------------------- #
                            #    set the definitive allocating matrix for current agent   #
                            # ----------------------------------------------------------- #
                            for j in range(len(goods_list_param)):
                                if j == agent[agent_key][i]:
                                    # ------------------------------------------------------- #
                                    #    if current good(index) allocated to current agent:   #
                                    # ------------------------------------------------------- #
                                    random_allocated_matrices[index_of_allocated_matrix][agent_key][j] = 1
                                    del goods_list_for_each_steps[j]
                                else:
                                    random_allocated_matrices[index_of_allocated_matrix][agent_key][j] = 0
                            break
                        
            # --------------------------------------------------------------------------------------------------- #
            #    set last definitive allocating matrix (for last agent) in this random_allocated_matrices item:   #
            # --------------------------------------------------------------------------------------------------- #
            elif len(goods_list_for_each_steps) == 1:
                # ----------------------------------------------------------- #
                #    set the definitive allocating matrix for current agent   #
                # ----------------------------------------------------------- #
                for i in range(len(goods_list_param)):
                    if i == list(goods_list_for_each_steps.values())[0]:
                        # ------------------------------------------------------- #
                        #    if current good(index) allocated to current agent:   #
                        # ------------------------------------------------------- #
                        random_allocated_matrices[index_of_allocated_matrix][agent_key][i] = 1
                    else:
                        random_allocated_matrices[index_of_allocated_matrix][agent_key][i] = 0

        # --------------------------------------------------------- #
        #    prepare the key for store the next allocated matrix:   #
        # --------------------------------------------------------- #
        index_of_allocated_matrix += 1
# ---------------------------------------------------------------------------- #


def calculate_final_matrix(matrices_param):
    global final_matrix, number_of_growth_RSD_items
    for key in matrices_param:
        matrix = matrices_param[key]
        for agent_index in matrix:
            agent = matrix[agent_index]
            # --------------------------------------------------------------------------------------------------- #
            #    if final matrix had not prepared for current agent possibilities calculateing, then prepare it:    #
            # --------------------------------------------------------------------------------------------------- #
            try:
                # --------------------------------- #
                #    if this dictionary created?    #
                # --------------------------------- #
                final_matrix[agent_index][0]
            except:
                # ------------------------------------------------------------------------------------------ #
                #    if not, then prepare the dictionary to storing(summation) good indexes value of each agents:    #
                # ------------------------------------------------------------------------------------------ #
                final_matrix[agent_index] = {}    
            # ------------------------------------------------------------------- #
            #    summation the result of each allocated matrices for each agent   #
            # ------------------------------------------------------------------- #
            for good_index in agent:
                current_allocate_possibility = agent[good_index]
                if good_index in final_matrix[agent_index]:
                    final_matrix[agent_index][good_index] += current_allocate_possibility
                else:
                    final_matrix[agent_index][good_index] = current_allocate_possibility
    # --------------------------------------------------- #
    #    finally, for special final possibility showing   #
    # --------------------------------------------------- #
    for agent_index in final_matrix:
        agent = final_matrix[agent_index]
        for good_index in agent:
            acumulated_results = agent[good_index]
            if acumulated_results != 0:
                final_matrix[agent_index][good_index] = str(acumulated_results) + "/" + str(number_of_growth_RSD_items)
# ---------------------------------------------------------------------------- #


number_of_agents = len(agents)
if number_of_agents > 1:
    growth_RSD_items = {}
    RSD_item_number = 0
    last_RSD_item_number = 0
    set_order_of_agents_items(agents, {}, 0)
    # ------------------------------------------------------------------------------------------------------------ #
    #    dictionary => index of growth RSD items => order of each agents => agents index => agents preferences index:   #
    # ------------------------------------------------------------------------------------------------------------ #
    # pretty(growth_RSD_items)


    # -------------------------------------------------------------------------- #
    #    number of goods(services) that we want to allocate = number of agents   #
    # -------------------------------------------------------------------------- #
    goods_list = {}
    for i in range(0, number_of_agents, 1):
        goods_list[i] = i
        
    number_of_growth_RSD_items = len(growth_RSD_items)
    # ---------------------------------------------------- #
    #    prepare a variable to store allocated matrices:   #
    # ---------------------------------------------------- #
    random_allocated_matrices = {}
    set_various_allocates(growth_RSD_items, goods_list)
    # ------------------------------------------------------------------------------------------------------------------------------- #
    #    dictionary => index of allocated {matrices} => order of each agents => agents index => agents good(service) allocated {matrix} :  #
    # ------------------------------------------------------------------------------------------------------------------------------- #
    # pretty(random_allocated_matrices)


    # ------------------------------------------------------------------------------- #
    #    prepare a variable to calculate good allocate possibility for each agents:   #
    # ------------------------------------------------------------------------------- #
    final_matrix = {}
    calculate_final_matrix(random_allocated_matrices)
    # ----------------------------------------------------------------------- #
    #    dictionary => agents index => agent good(service) allocate possibility:   #
    # ----------------------------------------------------------------------- #
    # pprint(final_matrix)
    pretty(final_matrix)
# ---------------------------------------------------------------------------- #
