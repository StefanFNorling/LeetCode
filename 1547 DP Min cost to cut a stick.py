class Solution:
    def minCost(self, n: int, cuts: list) -> int:
        cuts.extend([0,n])
        number_of_cuts = len(cuts)
        cut_values = [[0] * number_of_cuts for i in range(number_of_cuts)]
        cuts.sort()
        for dist_btwn_cut_indeces in range(2,number_of_cuts):
            for cut_index in range(number_of_cuts - dist_btwn_cut_indeces):
                cut_values[cut_index][cut_index + dist_btwn_cut_indeces] = min([cut_values[cut_index][middle_cut] + cut_values[middle_cut][cut_index + dist_btwn_cut_indeces] for middle_cut in range(cut_index + 1, cut_index + dist_btwn_cut_indeces)]) + cuts[cut_index + dist_btwn_cut_indeces] - cuts[cut_index]
        return cut_values[0][number_of_cuts - 1]