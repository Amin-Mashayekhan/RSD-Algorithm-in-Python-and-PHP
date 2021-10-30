<?php

/* -------------------------------- samples -------------------------------- */
// $agents = [
//     0 => [6, 3, 2, 8, 5, 1, 7, 4, 0],
//     1 => [6, 3, 1, 2, 5, 7, 8, 0, 4],
//     2 => [6, 0, 2, 8, 1, 0, 7, 5, 4],
//     3 => [6, 0, 1, 8, 3, 2, 7, 4, 5],
//     4 => [6, 5, 2, 8, 0, 4, 7, 3, 1],
//     5 => [6, 5, 2, 1, 4, 7, 3, 8, 0],
//     6 => [6, 5, 2, 8, 1, 4, 7, 3, 0],
//     7 => [6, 5, 2, 8, 1, 4, 7, 3, 0],
//     8 => [6, 5, 2, 1, 4, 7, 8, 3, 0],
// ];

// $agents = [
//     0 => [6, 3, 2, 5, 1, 7, 4, 0],
//     1 => [6, 3, 1, 2, 5, 7, 0, 4],
//     2 => [6, 0, 2, 1, 0, 7, 5, 4],
//     3 => [6, 0, 1, 3, 2, 7, 4, 5],
//     4 => [6, 5, 2, 0, 4, 7, 3, 1],
//     5 => [6, 5, 2, 1, 4, 7, 3, 0],
//     6 => [6, 5, 2, 1, 4, 7, 3, 0],
//     7 => [6, 5, 2, 1, 4, 7, 3, 0],
// ];

// $agents = [
//     0 => [6, 3, 2, 5, 1, 4, 0],
//     1 => [6, 3, 1, 2, 5, 0, 4],
//     2 => [6, 0, 2, 1, 0, 5, 4],
//     3 => [6, 0, 1, 3, 2, 4, 5],
//     4 => [6, 5, 2, 0, 4, 3, 1],
//     5 => [6, 5, 2, 1, 4, 3, 0],
//     6 => [6, 5, 2, 1, 4, 3, 0],
// ];

// $agents = [
//     0 => [3, 2, 5, 1, 4, 0],
//     1 => [3, 1, 2, 5, 0, 4],
//     2 => [0, 2, 1, 0, 5, 4],
//     3 => [0, 1, 3, 2, 4, 5],
//     4 => [5, 2, 0, 4, 3, 1],
//     5 => [5, 2, 1, 4, 3, 0],
// ];

// $agents = [
//     0 => [3 , 2 , 1 , 4 , 0],
//     1 => [3 , 1 , 2 , 0 , 4],
//     2 => [0 , 2 , 1 , 0 , 4],
//     3 => [0 , 1 , 3 , 2 , 4],
//     4 => [2 , 0 , 4 , 3 , 1],
// ]; 

$agents = [
    0 => [0, 1, 2, 3],
    1 => [0, 1, 2, 3],
    2 => [2, 0, 1, 3],
    3 => [2, 3, 0, 1],
];

// $agents = [
//     0 => [0 , 1 , 2],
//     1 => [0 , 1 , 2],
//     2 => [1 , 2 , 0],
// ]; 

// $agents = [
//     0 => [1 , 0],
//     1 => [1 , 0],
// ]; 

/* -------------------------------------------------------------------------- */



$number_of_agents =  count($agents);
if ($number_of_agents > 1) {
    $growth_RSD_items = [];
    $RSD_item_number = 0;
    $last_RSD_item_number = 0;
    set_order_of_agents_items($agents, [], 0);


    /* ---------------------------------------------------------------------------------------------------------- */
    /*   array => index of growth RSD items => order of each agents => agents index => agents preferences index   */
    /* ---------------------------------------------------------------------------------------------------------- */
    // echo '<pre>';
    // print_r($growth_RSD_items);
    // echo  '</pre>';


    /* ------------------------------------------------------------------------- */
    /*   number of agents = number of goods(services) that we want to allocate   */
    /* ------------------------------------------------------------------------- */
    $goods_list = [];
    for ($i = 0; $i < $number_of_agents; $i++) {
        array_push($goods_list, $i);
    }
    $number_of_growth_RSD_items = count($growth_RSD_items);
    $random_allocated_matrices = [];
    set_various_allocates($growth_RSD_items, $goods_list);


    /* ----------------------------------------------------------------------------------------------------------------------------- */
    /*   array => index of allocated {matrices} => order of each agents => agents index => agents good(service) allocated {matrix}   */
    /* ----------------------------------------------------------------------------------------------------------------------------- */
    // echo '<pre>';
    // print_r(($random_allocated_matrices));
    // echo '</pre>';


    $final_matrix = [];
    calculate_final_matrix($random_allocated_matrices);


    /* --------------------------------------------------------------------- */
    /*   array => agents index => agent good(service) allocate possibility   */
    /* --------------------------------------------------------------------- */
    echo '<pre>';
    print_r($final_matrix);
    echo '</pre>';
}



function set_order_of_agents_items($agents_param, $sorted_agents_param, $current_order_param)
{
    global $growth_RSD_items, $last_RSD_item_number;
    foreach ($agents_param as $key => $agent) {
        $order = $current_order_param;
        /* ------------------------------------------------------ */
        /*   for each allocating item, clear last sorted agent:   */
        /* ------------------------------------------------------ */
        $sorted_agents_param[$order] = [];
        if (count($agents_param) > 1) {
            $sorted_agents_param[$order][$key] = $agents_param[$key];
            /* -------------------------------------------------------- */
            /*   clear current sorted agent for next sorting step(s):   */
            /* -------------------------------------------------------- */
            $result_of_current_step = $agents_param;
            unset($result_of_current_step[$key]);
            $next_order = $order + 1;
            set_order_of_agents_items($result_of_current_step, $sorted_agents_param, $next_order);
        } elseif (count($agents_param) == 1) {
            $sorted_agents_param[$order][$key] = $agents_param[$key];
            $growth_RSD_items[$last_RSD_item_number] = $sorted_agents_param;
            $last_RSD_item_number += 1;
        }
    }
}



function set_various_allocates($growth_RSD_items_param, $goods_list_param)
{
    global $random_allocated_matrices, $number_of_growth_RSD_items;
    /* ----------------------------------------------------- */
    /*   here, number of allocated matrices begins from 0:   */
    /* ----------------------------------------------------- */
    $index_of_allocated_matrix = 0;
    foreach ($growth_RSD_items_param as $index_of_item => $item) {
        /* ---------------------------------------------- */
        /*   here, agents tendency index begins from 0:   */
        /* ---------------------------------------------- */
        $goods_list_for_each_steps = $goods_list_param;
        foreach ($item as $order => $agent) {
            $best_remained_good_index_for_agent = 0;
            if (count($goods_list_for_each_steps) > 1) {
                if (in_array($agent[key($agent)][$best_remained_good_index_for_agent], $goods_list_for_each_steps)) {
                    /* ---------------------------------------------------------- */
                    /*   set the definitive allocating matrix for current agent   */
                    /* ---------------------------------------------------------- */
                    for ($i = 0; $i < count($goods_list_param); $i++) {
                        if ($i == $agent[key($agent)][$best_remained_good_index_for_agent]) {
                            // $random_allocated_matrices[$index_of_allocated_matrix][key($agent)][] = 1 / $number_of_growth_RSD_items;
                            $random_allocated_matrices[$index_of_allocated_matrix][key($agent)][] = 1;
                            unset($goods_list_for_each_steps[$i]);
                        } else {
                            $random_allocated_matrices[$index_of_allocated_matrix][key($agent)][] = 0;
                        }
                    }
                } else {
                    /* ---------------------------------------------------------------- */
                    /*   now ++$best_remained_good_index_for_agent becomes equal to 1:  */
                    /* ---------------------------------------------------------------- */
                    for ($i = 1; $i < count($goods_list_param); $i++) {
                        if (in_array($agent[key($agent)][$i], $goods_list_for_each_steps)) {
                            /* ---------------------------------------------------------- */
                            /*   set the definitive allocating matrix for current agent   */
                            /* ---------------------------------------------------------- */
                            for ($j = 0; $j < count($goods_list_param); $j++) {
                                if ($j == $agent[key($agent)][$i]) {
                                    // $random_allocated_matrices[$index_of_allocated_matrix][key($agent)][] = 1 / $number_of_growth_RSD_items;
                                    $random_allocated_matrices[$index_of_allocated_matrix][key($agent)][] = 1;
                                    unset($goods_list_for_each_steps[$j]);
                                } else {
                                    $random_allocated_matrices[$index_of_allocated_matrix][key($agent)][] = 0;
                                }
                            }
                            break;
                        }
                    }
                }
            } elseif (count($goods_list_for_each_steps) == 1) {
                /* ---------------------------------------------------------- */
                /*   set the definitive allocating matrix for current agent   */
                /* ---------------------------------------------------------- */
                for ($i = 0; $i < count($goods_list_param); $i++) {
                    if ($i == $goods_list_for_each_steps[key($goods_list_for_each_steps)]) {
                        // $random_allocated_matrices[$index_of_allocated_matrix][key($agent)][] = 1 / $number_of_growth_RSD_items;
                        $random_allocated_matrices[$index_of_allocated_matrix][key($agent)][] = 1;
                    } else {
                        $random_allocated_matrices[$index_of_allocated_matrix][key($agent)][] = 0;
                    }
                }
            }
        }
        $index_of_allocated_matrix += 1;
    }

    /* ---------------------------------------------------------------------------- */
    /*   finally, sorting the random allocated matrices associate to agents index   */
    /* ---------------------------------------------------------------------------- */
    // foreach ($random_allocated_matrices as $key => $matrix) {
    // ksort($random_allocated_matrices[$key]);
    //     foreach ($matrix as $agent_order => $agent) {
    //         uasort($random_allocated_matrices[$key], function($a , $b){
    //             return key($a) <= key($b) ? -1 : 1;
    //         });
    //     }
    // }

}



function calculate_final_matrix($matrices_param)
{
    global $final_matrix, $number_of_growth_RSD_items;
    foreach ($matrices_param as $key => $matrix) {
        foreach ($matrix as $agent_index => $agent) {
            foreach ($agent as $good_index => $current_allocate_possobility) {
                if (isset($final_matrix[$agent_index][$good_index])) {
                    $final_matrix[$agent_index][$good_index] += $current_allocate_possobility;
                } else {
                    $final_matrix[$agent_index][$good_index] = $current_allocate_possobility;
                }
            }
        }
    }

    /* ---------------------------------------------------------------------------- */
    /*   finally, for special possibility showing                                   */
    /* ---------------------------------------------------------------------------- */
    foreach ($final_matrix as $agent_index => $agent) {
        foreach ($agent as $good_index => $acumulated_results) {
            if ($acumulated_results != 0) {
                $final_matrix[$agent_index][$good_index] = $acumulated_results . '/' . $number_of_growth_RSD_items;
            }
        }
    }
}
?>