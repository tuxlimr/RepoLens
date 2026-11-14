# Project structure: TheAlgorithms/Python

**Analysed commit:** `30507bbe41397065728167fb09aa820f9fce8dc7`

**Commit reference:** [30507bbe41397065728167fb09aa820f9fce8dc7](https://github.com/TheAlgorithms/Python/commit/30507bbe41397065728167fb09aa820f9fce8dc7)

**Tree at this commit:** [TheAlgorithms/Python@30507bbe4139](https://github.com/TheAlgorithms/Python/tree/30507bbe41397065728167fb09aa820f9fce8dc7)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | TheAlgorithms/Python |
| Description | All Algorithms implemented in Python |
| Stars | 226113 |
| Forks | 51323 |
| Licence | MIT |
| Language | Python |
| Default branch | master |
| Analysed commit | `30507bbe41397065728167fb09aa820f9fce8dc7` |
| Retrieved at | 2026-11-14T19:06:01.118915+00:00 |
| Files in this snapshot | 800 |

## Directory tree

```text
.devcontainer/  (4 files)
  Dockerfile
  README.md
  devcontainer.json
  post_install
.github/  (20 files)
  ISSUE_TEMPLATE/  (4 files)
    bug_report.yml
    config.yml
    feature_request.yml
    other.yml
  skills/  (3 files)
    code-review/  (1 files)
      … 1 files under this directory
    new-pull-request/  (1 files)
      … 1 files under this directory
    review-open-issue/  (1 files)
      … 1 files under this directory
  workflows/  (8 files)
    build.yml
    devcontainer_ci.yml
    directory_writer.yml
    hacktoberfest_prep.yml
    project_euler.yml
    ruff.yml
    sphinx.yml
    ty.yml
  CODEOWNERS
  dependabot.yml
  pull_request_template.md
  stale.yml
  zizmor.yml
audio_filters/  (7 files)
  README.md
  __init__.py
  butterworth_filter.py
  equal_loudness_filter.py
  iir_filter.py
  loudness_curve.json
  show_response.py
backtracking/  (24 files)
  README.md
  __init__.py
  all_combinations.py
  all_permutations.py
  all_subsequences.py
  coloring.py
  combination_sum.py
  crossword_puzzle_solver.py
  generate_parentheses.py
  generate_parentheses_iterative.py
  hamiltonian_cycle.py
  knight_tour.py
  m_coloring_problem.py
  match_word_pattern.py
  minimax.py
  n_queens.py
  n_queens_math.py
  power_sum.py
  rat_in_maze.py
  sudoku.py
  sum_of_subsets.py
  word_break.py
  word_ladder.py
  word_search.py
bit_manipulation/  (33 files)
  README.md
  __init__.py
  binary_and_operator.py
  binary_coded_decimal.py
  binary_count_setbits.py
  binary_count_trailing_zeros.py
  binary_or_operator.py
  binary_shifts.py
  binary_twos_complement.py
  binary_xor_operator.py
  bitwise_addition_recursive.py
  count_1s_brian_kernighan_method.py
  count_number_of_one_bits.py
  excess_3_code.py
  fast_walsh_hadamard_transform.py
  find_previous_power_of_two.py
  find_unique_number.py
  gray_code_sequence.py
  highest_set_bit.py
  index_of_rightmost_set_bit.py
  is_even.py
  is_power_of_two.py
  largest_pow_of_two_le_num.py
  missing_number.py
  … 9 more files
blockchain/  (8 files)
  README.md
  __init__.py
  diophantine_equation.py
  merkle_tree.py
  proof_of_stake.py
  proof_of_work.py
  simple_blockchain.py
  simple_proof_of_work.py
boolean_algebra/  (14 files)
  README.md
  __init__.py
  and_gate.py
  imply_gate.py
  karnaugh_map_simplification.py
  multiplexer.py
  nand_gate.py
  nimply_gate.py
  nor_gate.py
  not_gate.py
  or_gate.py
  quine_mc_cluskey.py
  xnor_gate.py
  xor_gate.py
cellular_automata/  (9 files)
  README.md
  __init__.py
  conways_game_of_life.py
  elementary_cellular_automaton.py
  game_of_life.py
  langtons_ant.py
  nagel_schrekenberg.py
  one_dimensional.py
  wa_tor.py
ciphers/  (55 files)
  README.md
  __init__.py
  a1z26.py
  affine_cipher.py
  atbash.py
  autokey.py
  baconian_cipher.py
  base16.py
  base32.py
  base58.py
  base64_cipher.py
  base85.py
  beaufort_cipher.py
  bifid.py
  brute_force_caesar_cipher.py
  caesar_cipher.py
  columnar_transposition.py
  cryptomath_module.py
  decrypt_caesar_with_chi_squared.py
  des_ecb.py
  deterministic_miller_rabin.py
  diffie.py
  diffie_hellman.py
  elgamal_key_generator.py
  … 31 more files
computer_vision/  (13 files)
  README.md
  __init__.py
  flip_augmentation.py
  gramian.py
  haralick_descriptors.py
  harris_corner.py
  horn_schunck.py
  intensity_based_segmentation.py
  mean_threshold.py
  mosaic_augmentation.py
  otsu_threshold.py
  pooling_functions.py
  vision_transformer.py
conversions/  (42 files)
  README.md
  __init__.py
  astronomical_length_scale_conversion.py
  base64_to_binary.py
  binary_to_base64.py
  binary_to_decimal.py
  binary_to_excess3.py
  binary_to_gray.py
  binary_to_gray_code.py
  binary_to_hexadecimal.py
  binary_to_octal.py
  convert_number_to_words.py
  decimal_to_any.py
  decimal_to_binary.py
  decimal_to_hexadecimal.py
  decimal_to_octal.py
  endianness.py
  energy_conversions.py
  excel_title_to_column.py
  hex_to_bin.py
  hex_to_rgb.py
  hexadecimal_to_decimal.py
  int_to_negative_binary_base.py
  ipv4_conversion.py
  … 18 more files
data_compression/  (11 files)
  README.md
  __init__.py
  burrows_wheeler.py
  coordinate_compression.py
  huffman.py
  lempel_ziv.py
  lempel_ziv_decompress.py
  lz77.py
  move_to_front.py
  peak_signal_to_noise_ratio.py
  run_length_encoding.py
data_structures/  (151 files)
  arrays/  (21 files)
    __init__.py
    dynamic_array.py
    equilibrium_index_in_array.py
    find_triplets_with_0_sum.py
    gas_station.py
    index_2d_array_in_1d.py
    kth_largest_element.py
    median_two_array.py
    merge_intervals.py
    merge_sorted.py
    monotonic_array.py
    pairs_with_given_sum.py
    pairwise_iteration.py
    permutations.py
    prefix_sum.py
    product_sum.py
    reverse_array.py
    rotate_array.py
    set_matrix_zeroes.py
    sparse_table.py
    sudoku_solver.py
  binary_tree/  (37 files)
    README.md
    __init__.py
    avl_tree.py
    basic_binary_tree.py
    binary_search_tree.py
    binary_search_tree_recursive.py
    binary_tree_maximum_path_sum.py
    binary_tree_mirror.py
    binary_tree_node_sum.py
    binary_tree_path_sum.py
    binary_tree_traversals.py
    diameter_of_binary_tree.py
    diff_views_of_binary_tree.py
    distribute_coins.py
    fenwick_tree.py
    flatten_binarytree_to_linkedlist.py
    floor_and_ceiling.py
    inorder_tree_traversal_2022.py
    is_sorted.py
    is_sum_tree.py
    lazy_segment_tree.py
    lowest_common_ancestor.py
    maximum_fenwick_tree.py
    maximum_sum_bst.py
    … 13 more files
  disjoint_set/  (3 files)
    __init__.py
    alternate_disjoint_set.py
    disjoint_set.py
  hashing/  (11 files)
    number_theory/  (2 files)
      … 2 files under this directory
    tests/  (2 files)
      … 2 files under this directory
    __init__.py
    bloom_filter.py
    double_hash.py
    hash_map.py
    hash_table.py
    hash_table_with_linked_list.py
    quadratic_probing.py
  heap/  (8 files)
    __init__.py
    binomial_heap.py
    heap.py
    heap_generic.py
    max_heap.py
    min_heap.py
    randomized_heap.py
    skew_heap.py
  kd_tree/  (9 files)
    example/  (3 files)
      … 3 files under this directory
    tests/  (2 files)
      … 2 files under this directory
    __init__.py
    build_kdtree.py
    kd_node.py
    nearest_neighbour_search.py
  linked_list/  (23 files)
    __init__.py
    circular_linked_list.py
    deque_doubly.py
    doubly_linked_list.py
    doubly_linked_list_two.py
    floyds_cycle_detection.py
    from_sequence.py
    has_loop.py
    is_palindrome.py
    kth_element_from_end.py
    merge_sort_linked_list.py
    merge_two_lists.py
    middle_element_of_linked_list.py
    partition_linked_list.py
    print_reverse.py
    remove_nth_node_from_end_of_list.py
    reverse_k_group.py
    rotate_to_the_right.py
    singly_linked_list.py
    skip_list.py
    sorted_linked_list.py
    swap_nodes.py
    xor_linked_list.py
  queues/  (10 files)
    __init__.py
    circular_queue.py
    circular_queue_linked_list.py
    double_ended_queue.py
    linked_queue.py
    monotonic_queue.py
    priority_queue_using_list.py
    queue_by_list.py
    queue_by_two_stacks.py
    queue_on_pseudo_stack.py
  stacks/  (18 files)
    __init__.py
    balanced_parentheses.py
    dijkstras_two_stack_algorithm.py
    infix_to_postfix_conversion.py
    infix_to_prefix_conversion.py
    kth_next_greater_element.py
    largest_rectangle_histogram.py
    lexicographical_numbers.py
    next_greater_element.py
    postfix_evaluation.py
    postfix_to_infix_conversion.py
    prefix_evaluation.py
    stack.py
    stack_tracking_min_max.py
    stack_using_two_queues.py
    stack_with_doubly_linked_list.py
    stack_with_singly_linked_list.py
    stock_span_problem.py
  suffix_tree/  (7 files)
    example/  (2 files)
      … 2 files under this directory
    tests/  (2 files)
      … 2 files under this directory
    __init__.py
    suffix_tree.py
    suffix_tree_node.py
  trie/  (3 files)
    __init__.py
    radix_tree.py
    trie.py
  __init__.py
digital_image_processing/  (32 files)
  dithering/  (2 files)
    __init__.py
    burkes.py
  edge_detection/  (2 files)
    __init__.py
    canny.py
  filters/  (9 files)
    __init__.py
    bilateral_filter.py
    convolve.py
    gabor_filter.py
    gaussian_filter.py
    laplacian_filter.py
    local_binary_pattern.py
    median_filter.py
    sobel_filter.py
  histogram_equalization/  (4 files)
    image_data/  (1 files)
      … 1 files under this directory
    output_data/  (1 files)
      … 1 files under this directory
    __init__.py
    histogram_stretch.py
  image_data/  (1 files)
    __init__.py
  morphological_operations/  (3 files)
    __init__.py
    dilation_operation.py
    erosion_operation.py
  resize/  (2 files)
    __init__.py
    resize.py
  rotation/  (2 files)
    __init__.py
    rotation.py
  __init__.py
  change_brightness.py
  change_contrast.py
  convert_to_negative.py
  index_calculation.py
  sepia.py
  test_digital_image_processing.py
divide_and_conquer/  (16 files)
  tests/  (2 files)
    __init__.py
    test_strassen_matrix_multiplication.py
  __init__.py
  closest_pair_of_points.py
  convex_hull.py
  heaps_algorithm.py
  heaps_algorithm_iterative.py
  inversions.py
  kth_order_statistic.py
  max_difference_pair.py
  max_subarray.py
  mergesort.py
  minimum_element_of_array.py
  peak.py
  power.py
  strassen_matrix_multiplication.py
docs/  (4 files)
  source/  (1 files)
    __init__.py
  __init__.py
  conf.py
  hacktober_2026_prep.md
dynamic_programming/  (53 files)
  __init__.py
  abbreviation.py
  all_construct.py
  bitmask.py
  catalan_numbers.py
  climbing_stairs.py
  combination_sum_iv.py
  edit_distance.py
  egg_dropping.py
  factorial.py
  fast_fibonacci.py
  fibonacci.py
  fizz_buzz.py
  floyd_warshall.py
  integer_partition.py
  iterating_through_submasks.py
  knapsack.py
  largest_divisible_subset.py
  longest_common_subsequence.py
  longest_common_substring.py
  longest_increasing_subsequence.py
  longest_increasing_subsequence_iterative.py
  longest_increasing_subsequence_o_nlogn.py
  longest_palindromic_subsequence.py
  … 29 more files
electronics/  (24 files)
  __init__.py
  apparent_power.py
  builtin_voltage.py
  capacitor_equivalence.py
  carrier_concentration.py
  charging_capacitor.py
  charging_inductor.py
  circular_convolution.py
  coulombs_law.py
  electric_conductivity.py
  electric_power.py
  electrical_impedance.py
  full_wave_rectifier.py
  half_wave_rectifier.py
  ic_555_timer.py
  ind_reactance.py
  ohms_law.py
  power_factor_correction.py
  real_and_reactive_power.py
  resistor_color_code.py
  resistor_equivalence.py
  resonant_frequency.py
  star_delta_conversions.py
  wheatstone_bridge.py
file_transfer/  (6 files)
  tests/  (2 files)
    __init__.py
    test_send_file.py
  __init__.py
  mytext.txt
  receive_file.py
  send_file.py
financial/  (19 files)
  README.md
  __init__.py
  annuity_due_future_value.py
  equated_monthly_installments.py
  expected_shortfall.py
  exponential_moving_average.py
  fractional_differentiation.py
  interest.py
  kelly_criterion.py
  macaulay_duration.py
  ordinary_annuity_future_value.py
  present_value.py
  price_plus_tax.py
  sharpe_ratio.py
  simple_moving_average.py
  straight_line_depreciation.py
  streaming_moving_average.py
  time_and_half_pay.py
  value_at_risk.py
fractals/  (10 files)
  README.md
  __init__.py
  barnsley_fern.py
  hilbert_curve.py
  julia_sets.py
  koch_snowflake.py
  mandelbrot.py
  sierpinski_carpet.py
  sierpinski_triangle.py
  vicsek.py
fuzzy_logic/  (4 files)
  README.md
  __init__.py
  fuzzy_operations.py
  fuzzy_set_operations.py
genetic_algorithm/  (3 files)
  __init__.py
  basic_string.py
  travelling_salesman_problem.py
geodesy/  (4 files)
  __init__.py
  haversine_distance.py
  lamberts_ellipsoidal_distance.py
  radar_target_calculation.py
geometry/  (14 files)
  tests/  (3 files)
    __init__.py
    test_graham_scan.py
    test_jarvis_march.py
  __init__.py
  braik_mac_construction.py
  geometry.py
  graham_scan.py
  jarvis_march.py
  monotone_chain.py
  ramer_douglas_peucker.py
  rotating_calipers.py
  segment_intersection.py
  shoelace.py
  triangle.py
graphics/  (7 files)
  __init__.py
  bezier_curve.py
  bresenham_line_basic.py
  bresenham_line_generalized.py
  butterfly_pattern.py
  digital_differential_analyzer_line.py
  vector3_for_2d_rendering.py
graphs/  (73 files)
  tests/  (6 files)
    __init__.py
    test_edmonds_blossom_algorithm.py
    test_graphs_floyd_warshall.py
    test_johnson.py
    test_min_spanning_tree_kruskal.py
    test_min_spanning_tree_prim.py
  __init__.py
  a_star.py
  ant_colony_optimization_algorithms.py
  articulation_points.py
  basic_graphs.py
  bellman_ford.py
  bi_directional_dijkstra.py
  bidirectional_a_star.py
  bidirectional_breadth_first_search.py
  bidirectional_search.py
  boruvka.py
  breadth_first_search.py
  breadth_first_search_2.py
  breadth_first_search_shortest_path.py
  breadth_first_search_shortest_path_2.py
  breadth_first_search_zero_one_shortest_path.py
  check_bipatrite.py
  check_cycle.py
  connected_components.py
  deep_clone_graph.py
  depth_first_search.py
  depth_first_search_2.py
  dijkstra.py
  dijkstra_2.py
  … 43 more files
greedy_methods/  (13 files)
  __init__.py
  activity_selection.py
  best_time_to_buy_and_sell_stock.py
  fractional_cover_problem.py
  fractional_knapsack.py
  fractional_knapsack_2.py
  gas_station.py
  minimize_deviation_in_array.py
  minimum_coin_change.py
  minimum_waiting_time.py
  optimal_merge_pattern.py
  sliding_window.py
  smallest_range.py
hashes/  (16 files)
  README.md
  __init__.py
  adler32.py
  chaos_machine.py
  crc32.py
  djb2.py
  elf.py
  enigma_machine.py
  fletcher16.py
  hamming_code.py
  jenkins_one_at_a_time.py
  luhn.py
  md5.py
  sdbm.py
  sha1.py
  sha256.py
knapsack/  (8 files)
  tests/  (3 files)
    __init__.py
    test_greedy_knapsack.py
    test_knapsack.py
  README.md
  __init__.py
  greedy_knapsack.py
  knapsack.py
  recursive_approach_knapsack.py
linear_algebra/  (18 files)
  src/  (11 files)
    __init__.py
    conjugate_gradient.py
    gaussian_elimination_pivoting.py
    lib.py
    polynom_for_points.py
    power_iteration.py
    rank_of_matrix.py
    rayleigh_quotient.py
    schur_complement.py
    test_linear_algebra.py
    transformations_2d.py
  README.md
  __init__.py
  gauss_jordan.py
  gaussian_elimination.py
  jacobi_iteration_method.py
  lu_decomposition.py
  matrix_inversion.py
linear_programming/  (2 files)
  __init__.py
  simplex.py
machine_learning/  (50 files)
  forecasting/  (3 files)
    __init__.py
    ex_data.csv
    run.py
  local_weighted_learning/  (3 files)
    README.md
    __init__.py
    local_weighted_learning.py
  __init__.py
  apriori_algorithm.py
  astar.py
  automatic_differentiation.py
  data_transformations.py
  dbscan.py
  decision_tree.py
  dimensionality_reduction.py
  federated_averaging.py
  frequent_pattern_growth.py
  gaussian_mixture_model.py
  gaussian_naive_bayes.py
  gradient_boosting_classifier.py
  gradient_boosting_regressor.py
  gradient_descent.py
  k_means_clust.py
  k_medoids.py
  k_nearest_neighbors.py
  linear_discriminant_analysis.py
  linear_regression.py
  linear_regression_vectorized.py
  logistic_regression.py
  loss_functions.py
  mab.py
  … 20 more files
maths/  (21 files)
  __init__.py
  abs.py
  addition_without_arithmetic.py
  aliquot_sum.py
  allocation_number.py
  arc_length.py
  area.py
  area_under_curve.py
  autocorrelation.py
  average_absolute_deviation.py
  average_mean.py
  average_median.py
  average_mode.py
  bailey_borwein_plouffe.py
  base_neg2_conversion.py
  basic_maths.py
  bearing.py
  binary_exponentiation.py
  binary_multiplication.py
  binomial_coefficient.py
  binomial_distribution.py
.gitattributes
.gitignore
.gitpod.yml
.pre-commit-config.yaml
.python-version
AGENTS.md
CONTRIBUTING.md
DIRECTORY.md
LICENSE.md
README.md
SECURITY.md
index.md
```

## Entry points

- [linear_algebra/src/conjugate_gradient.py:176](https://github.com/TheAlgorithms/Python/blob/30507bbe41397065728167fb09aa820f9fce8dc7/linear_algebra/src/conjugate_gradient.py#L176)
- [linear_algebra/src/gaussian_elimination_pivoting.py:72](https://github.com/TheAlgorithms/Python/blob/30507bbe41397065728167fb09aa820f9fce8dc7/linear_algebra/src/gaussian_elimination_pivoting.py#L72)
- [linear_algebra/src/polynom_for_points.py:106](https://github.com/TheAlgorithms/Python/blob/30507bbe41397065728167fb09aa820f9fce8dc7/linear_algebra/src/polynom_for_points.py#L106)
- [linear_algebra/src/power_iteration.py:125](https://github.com/TheAlgorithms/Python/blob/30507bbe41397065728167fb09aa820f9fce8dc7/linear_algebra/src/power_iteration.py#L125)
- [linear_algebra/src/rank_of_matrix.py:90](https://github.com/TheAlgorithms/Python/blob/30507bbe41397065728167fb09aa820f9fce8dc7/linear_algebra/src/rank_of_matrix.py#L90)
- [linear_algebra/src/rayleigh_quotient.py:65](https://github.com/TheAlgorithms/Python/blob/30507bbe41397065728167fb09aa820f9fce8dc7/linear_algebra/src/rayleigh_quotient.py#L65)
- [linear_algebra/src/schur_complement.py:94](https://github.com/TheAlgorithms/Python/blob/30507bbe41397065728167fb09aa820f9fce8dc7/linear_algebra/src/schur_complement.py#L94)
- [backtracking/all_combinations.py:103](https://github.com/TheAlgorithms/Python/blob/30507bbe41397065728167fb09aa820f9fce8dc7/backtracking/all_combinations.py#L103)
- [backtracking/all_subsequences.py:102](https://github.com/TheAlgorithms/Python/blob/30507bbe41397065728167fb09aa820f9fce8dc7/backtracking/all_subsequences.py#L102)
- [backtracking/combination_sum.py:72](https://github.com/TheAlgorithms/Python/blob/30507bbe41397065728167fb09aa820f9fce8dc7/backtracking/combination_sum.py#L72)
- [backtracking/crossword_puzzle_solver.py:114](https://github.com/TheAlgorithms/Python/blob/30507bbe41397065728167fb09aa820f9fce8dc7/backtracking/crossword_puzzle_solver.py#L114)
- [backtracking/generate_parentheses.py:78](https://github.com/TheAlgorithms/Python/blob/30507bbe41397065728167fb09aa820f9fce8dc7/backtracking/generate_parentheses.py#L78)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| audio_filters package | library | Observed | Groups 5 file(s) under audio_filters package (observed from repository paths and static analysis). Observed top-level classes: EqualLoudnessFilter, FilterType, IIRFilter. Observed top-level functions: _numerator, _polys… |
| backtracking package | library | Observed | Groups 7 file(s) under backtracking package (observed from repository paths and static analysis). Observed top-level functions: backtrack, color, create_state_space_tree, generate_all_permutations, hamilton_cycle, is_sa… |
| bit_manipulation package | library | Observed | Groups 1 file(s) under bit_manipulation package (observed from repository paths and static analysis). |
| blockchain package | library | Observed | Groups 3 file(s) under blockchain package (observed from repository paths and static analysis). Observed top-level classes: Block, Blockchain, Validator. Observed top-level functions: choose_validator. |
| boolean_algebra package | library | Observed | Groups 1 file(s) under boolean_algebra package (observed from repository paths and static analysis). |
| cellular_automata package | library | Observed | Groups 1 file(s) under cellular_automata package (observed from repository paths and static analysis). |
| ciphers package | library | Observed | Groups 5 file(s) under ciphers package (observed from repository paths and static analysis). Observed top-level classes: BifidCipher, PolybiusCipher. Observed top-level functions: decrypt_caesar_with_chi_squared, find_m… |
| computer_vision package | library | Observed | Groups 2 file(s) under computer_vision package (observed from repository paths and static analysis). Observed top-level functions: otsu_threshold. |
| Configuration and deployment | config | Observed | Groups 1 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| conversions package | library | Observed | Groups 2 file(s) under conversions package (observed from repository paths and static analysis). Observed top-level functions: approximately_equal_hsv, hsv_to_rgb, rgb_to_hsv. |
| data_compression package | library | Observed | Groups 2 file(s) under data_compression package (observed from repository paths and static analysis). |
| data_structures package | library | Observed | Groups 36 file(s) under data_structures package (observed from repository paths and static analysis). Observed top-level classes: Bloom, CircularQueue, DisjointSet, HashTableWithLinkedList, KDNode, LinkedDeque. Observed… |
| digital_image_processing package | library | Observed | Groups 12 file(s) under digital_image_processing package (observed from repository paths and static analysis). Observed top-level classes: IndexCalculation. |
| divide_and_conquer package | library | Observed | Groups 1 file(s) under divide_and_conquer package (observed from repository paths and static analysis). |
| dynamic_programming package | library | Observed | Groups 3 file(s) under dynamic_programming package (observed from repository paths and static analysis). Observed top-level functions: max_product_subarray, minimum_subarray_sum. |
| electronics package | library | Observed | Groups 1 file(s) under electronics package (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 591 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: AStar, AVLtree, AdjacencyList, Angle, AssignmentUsingBitmask, BWTTransformDict. Observed… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| file_transfer package | library | Observed | Groups 1 file(s) under file_transfer package (observed from repository paths and static analysis). |
| financial package | library | Observed | Groups 1 file(s) under financial package (observed from repository paths and static analysis). |
| fractals package | library | Observed | Groups 1 file(s) under fractals package (observed from repository paths and static analysis). |
| fuzzy_logic package | library | Observed | Groups 1 file(s) under fuzzy_logic package (observed from repository paths and static analysis). |
| genetic_algorithm package | library | Observed | Groups 1 file(s) under genetic_algorithm package (observed from repository paths and static analysis). |
| geodesy package | library | Observed | Groups 1 file(s) under geodesy package (observed from repository paths and static analysis). |
| geometry package | library | Observed | Groups 1 file(s) under geometry package (observed from repository paths and static analysis). |
| graphics package | library | Observed | Groups 1 file(s) under graphics package (observed from repository paths and static analysis). |
| graphs package | library | Observed | Groups 14 file(s) under graphs package (observed from repository paths and static analysis). Observed top-level classes: BlossomAuxData, BlossomData, Dinic, DirectedGraph, DisjointSetTree, DisjointSetTreeNode. Observed… |
| greedy_methods package | library | Observed | Groups 2 file(s) under greedy_methods package (observed from repository paths and static analysis). Observed top-level functions: activity_selection. |
| hashes package | library | Observed | Groups 5 file(s) under hashes package (observed from repository paths and static analysis). Observed top-level functions: adler32, djb2, emitter_converter, receptor_converter, sdbm, text_from_bits. |
| knapsack package | library | Observed | Groups 1 file(s) under knapsack package (observed from repository paths and static analysis). |
| linear_algebra package | library | Observed | Groups 4 file(s) under linear_algebra package (observed from repository paths and static analysis). Observed top-level classes: Matrix, Vector. Observed top-level functions: axpy, projection, random_matrix, random_vecto… |
| linear_programming package | library | Observed | Groups 1 file(s) under linear_programming package (observed from repository paths and static analysis). |
| machine_learning package | library | Observed | Groups 6 file(s) under machine_learning package (observed from repository paths and static analysis). Observed top-level functions: document_frequency, inverse_document_frequency, mae, manual_accuracy, mbd, mse. |
| maths package | library | Observed | Groups 1 file(s) under maths package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 24 file(s) under tests (observed from repository paths and static analysis). Observed routes: PATCH socket.socket, PATCH builtins.open. Observed top-level classes: EdmondsBlossomAlgorithmTest, Test, TestClass, Te… |

## Important files

- `.devcontainer/Dockerfile` (container)
- `.devcontainer/devcontainer.json` (config)
- `.github/ISSUE_TEMPLATE/bug_report.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/ISSUE_TEMPLATE/feature_request.yml` (config)
- `.github/ISSUE_TEMPLATE/other.yml` (config)
- `.github/dependabot.yml` (config)
- `.github/stale.yml` (config)
- `.github/workflows/build.yml` (ci)
- `.github/workflows/devcontainer_ci.yml` (ci)
- `.github/workflows/directory_writer.yml` (ci)
- `.github/workflows/hacktoberfest_prep.yml` (ci)
- `.github/workflows/project_euler.yml` (ci)
- `.github/workflows/ruff.yml` (ci)
- `.github/workflows/sphinx.yml` (ci)
- `.github/workflows/ty.yml` (ci)
- `.github/zizmor.yml` (config)
- `.gitpod.yml` (config)
- `.pre-commit-config.yaml` (config)
- `audio_filters/loudness_curve.json` (config)

## Top-level layout

- `data_structures` — 151 analysed file(s)
- `graphs` — 73 analysed file(s)
- `ciphers` — 55 analysed file(s)
- `dynamic_programming` — 53 analysed file(s)
- `machine_learning` — 50 analysed file(s)
- `conversions` — 42 analysed file(s)
- `bit_manipulation` — 33 analysed file(s)
- `digital_image_processing` — 32 analysed file(s)
- `backtracking` — 24 analysed file(s)
- `electronics` — 24 analysed file(s)
- `maths` — 21 analysed file(s)
- `.github` — 20 analysed file(s)
- `financial` — 19 analysed file(s)
- `linear_algebra` — 18 analysed file(s)
- `divide_and_conquer` — 16 analysed file(s)
- `hashes` — 16 analysed file(s)
- `boolean_algebra` — 14 analysed file(s)
- `geometry` — 14 analysed file(s)
- `computer_vision` — 13 analysed file(s)
- `greedy_methods` — 13 analysed file(s)
- `(root files)` — 12 analysed file(s)
- `data_compression` — 11 analysed file(s)
- `fractals` — 10 analysed file(s)
- `cellular_automata` — 9 analysed file(s)
- `blockchain` — 8 analysed file(s)
- `knapsack` — 8 analysed file(s)
- `audio_filters` — 7 analysed file(s)
- `graphics` — 7 analysed file(s)
- `file_transfer` — 6 analysed file(s)
- `.devcontainer` — 4 analysed file(s)
- `docs` — 4 analysed file(s)
- `fuzzy_logic` — 4 analysed file(s)
- `geodesy` — 4 analysed file(s)
- `genetic_algorithm` — 3 analysed file(s)
- `linear_programming` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- File data_compression/huffman.py could not be parsed as Python (possible SyntaxError) and was skipped for AST analysis.
- File data_structures/arrays/sudoku_solver.py could not be parsed as Python (possible SyntaxError) and was skipped for AST analysis.
- File graphs/hopcroft_karp.py could not be parsed as Python (possible SyntaxError) and was skipped for AST analysis.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `30507bbe41397065728167fb09aa820f9fce8dc7` is the revision these paths and observations refer to.
