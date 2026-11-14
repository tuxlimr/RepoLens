# Project structure: keon/algorithms

**Analysed commit:** `bd1d152f9ec7331c69be662831610b003b10fc7a`

**Commit reference:** [bd1d152f9ec7331c69be662831610b003b10fc7a](https://github.com/keon/algorithms/commit/bd1d152f9ec7331c69be662831610b003b10fc7a)

**Tree at this commit:** [keon/algorithms@bd1d152f9ec7](https://github.com/keon/algorithms/tree/bd1d152f9ec7331c69be662831610b003b10fc7a)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | keon/algorithms |
| Description | Minimal examples of data structures and algorithms in Python |
| Stars | 25597 |
| Forks | 4706 |
| Licence | MIT |
| Language | Python |
| Default branch | main |
| Analysed commit | `bd1d152f9ec7331c69be662831610b003b10fc7a` |
| Retrieved at | 2026-11-14T19:07:29.511283+00:00 |
| Files in this snapshot | 444 |

## Directory tree

```text
.github/  (2 files)
  workflows/  (2 files)
    publish.yml
    python-app.yml
algorithms/  (406 files)
  array/  (20 files)
    __init__.py
    delete_nth.py
    flatten.py
    garage.py
    josephus.py
    limit.py
    longest_non_repeat.py
    max_ones_index.py
    merge_intervals.py
    missing_ranges.py
    move_zeros.py
    n_sum.py
    plus_one.py
    remove_duplicates.py
    rotate.py
    summarize_ranges.py
    three_sum.py
    top_1.py
    trimmean.py
    two_sum.py
  backtracking/  (17 files)
    __init__.py
    add_operators.py
    anagram.py
    array_sum_combinations.py
    combination_sum.py
    factor_combinations.py
    find_words.py
    generate_abbreviations.py
    generate_parenthesis.py
    letter_combination.py
    minimax.py
    palindrome_partitioning.py
    pattern_match.py
    permute.py
    permute_unique.py
    subsets.py
    subsets_unique.py
  bit_manipulation/  (21 files)
    __init__.py
    add_bitwise_operator.py
    binary_gap.py
    bit_operation.py
    bytes_int_conversion.py
    count_flips_to_convert.py
    count_ones.py
    find_difference.py
    find_missing_number.py
    flip_bit_longest_sequence.py
    gray_code.py
    has_alternative_bit.py
    insert_bit.py
    power_of_two.py
    remove_bit.py
    reverse_bits.py
    single_number.py
    single_number2.py
    single_number3.py
    subsets.py
    swap_pair.py
  common/  (4 files)
    __init__.py
    graph.py
    list_node.py
    tree_node.py
  compression/  (5 files)
    __init__.py
    elias.py
    huffman_coding.py
    lzw_compression.py
    rle_compression.py
  data_structures/  (21 files)
    __init__.py
    avl_tree.py
    b_tree.py
    bst.py
    fenwick_tree.py
    graph.py
    hash_table.py
    heap.py
    iterative_segment_tree.py
    kd_tree.py
    linked_list.py
    priority_queue.py
    queue.py
    red_black_tree.py
    segment_tree.py
    separate_chaining_hash_table.py
    sqrt_decomposition.py
    stack.py
    trie.py
    union_find.py
    veb_tree.py
  dynamic_programming/  (27 files)
    __init__.py
    bitmask.py
    buy_sell_stock.py
    climbing_stairs.py
    coin_change.py
    combination_sum.py
    count_paths_dp.py
    edit_distance.py
    egg_drop.py
    fib.py
    hosoya_triangle.py
    house_robber.py
    int_divide.py
    job_scheduling.py
    k_factor.py
    knapsack.py
    longest_common_subsequence.py
    longest_increasing.py
    matrix_chain_order.py
    max_product_subarray.py
    max_subarray.py
    min_cost_path.py
    num_decodings.py
    planting_trees.py
    … 3 more files
  graph/  (41 files)
    __init__.py
    a_star.py
    all_factors.py
    all_pairs_shortest_path.py
    bellman_ford.py
    blossom.py
    check_bipartite.py
    check_digraph_strongly_connected.py
    clone_graph.py
    count_connected_number_of_component.py
    count_islands_bfs.py
    count_islands_dfs.py
    count_islands_unionfind.py
    cycle_detection.py
    dijkstra.py
    dijkstra_heapq.py
    find_all_cliques.py
    find_path.py
    graph.py
    kahns_algorithm.py
    markov_chain.py
    maximum_flow.py
    maximum_flow_bfs.py
    maximum_flow_dfs.py
    … 17 more files
  greedy/  (3 files)
    __init__.py
    gale_shapley.py
    max_contiguous_subsequence_sum.py
  heap/  (5 files)
    __init__.py
    k_closest_points.py
    merge_sorted_k_lists.py
    skyline.py
    sliding_window_max.py
  linked_list/  (17 files)
    __init__.py
    add_two_numbers.py
    copy_random_pointer.py
    delete_node.py
    first_cyclic_node.py
    intersection.py
    is_cyclic.py
    is_palindrome.py
    is_sorted.py
    kth_to_last.py
    merge_two_list.py
    partition.py
    remove_duplicates.py
    remove_range.py
    reverse.py
    rotate_list.py
    swap_in_pairs.py
  map/  (8 files)
    __init__.py
    is_anagram.py
    is_isomorphic.py
    longest_common_substring.py
    longest_palindromic_subsequence.py
    randomized_set.py
    valid_sudoku.py
    word_pattern.py
  math/  (45 files)
    __init__.py
    base_conversion.py
    chebyshev_distance.py
    chinese_remainder_theorem.py
    combination.py
    cosine_similarity.py
    decimal_to_binary_ip.py
    diffie_hellman_key_exchange.py
    distance_between_two_points.py
    euler_totient.py
    extended_gcd.py
    factorial.py
    fft.py
    find_order_simple.py
    find_primitive_root_simple.py
    gcd.py
    generate_strobogrammtic.py
    geometric_mean.py
    goldbach.py
    hailstone.py
    is_strobogrammatic.py
    krishnamurthy_number.py
    linear_regression.py
    magic_number.py
    … 21 more files
  matrix/  (17 files)
    __init__.py
    bomb_enemy.py
    cholesky_matrix_decomposition.py
    copy_transform.py
    count_paths.py
    crout_matrix_decomposition.py
    matrix_exponentiation.py
    matrix_inversion.py
    multiply.py
    rotate_image.py
    search_in_sorted_matrix.py
    sort_matrix_diagonally.py
    sparse_dot_vector.py
    sparse_mul.py
    spiral_traversal.py
    sudoku_validator.py
    sum_sub_squares.py
  queue/  (5 files)
    __init__.py
    max_sliding_window.py
    moving_average.py
    reconstruct_queue.py
    zigzagiterator.py
  searching/  (17 files)
    __init__.py
    binary_search.py
    exponential_search.py
    find_min_rotate.py
    first_occurrence.py
    generalized_binary_search.py
    interpolation_search.py
    jump_search.py
    last_occurrence.py
    linear_search.py
    next_greatest_letter.py
    search_insert.py
    search_range.py
    search_rotate.py
    sentinel_search.py
    ternary_search.py
    two_sum.py
  set/  (4 files)
    __init__.py
    find_keyboard_row.py
    randomized_set.py
    set_covering.py
  sorting/  (25 files)
    __init__.py
    bead_sort.py
    bitonic_sort.py
    bogo_sort.py
    bubble_sort.py
    bucket_sort.py
    cocktail_shaker_sort.py
    comb_sort.py
    counting_sort.py
    cycle_sort.py
    exchange_sort.py
    gnome_sort.py
    heap_sort.py
    insertion_sort.py
    meeting_rooms.py
    merge_sort.py
    pancake_sort.py
    pigeonhole_sort.py
    quick_sort.py
    radix_sort.py
    selection_sort.py
    shell_sort.py
    sort_colors.py
    stooge_sort.py
    … 1 more files
  stack/  (10 files)
    __init__.py
    is_consecutive.py
    is_sorted.py
    longest_abs_path.py
    ordered_stack.py
    remove_min.py
    simplify_path.py
    stutter.py
    switch_pairs.py
    valid_parenthesis.py
  streaming/  (3 files)
    __init__.py
    misra_gries.py
    one_sparse_recovery.py
  string/  (47 files)
    __init__.py
    add_binary.py
    alphabet_board_path.py
    atbash_cipher.py
    breaking_bad.py
    caesar_cipher.py
    check_pangram.py
    contain_string.py
    count_binary_substring.py
    decode_string.py
    delete_reoccurring.py
    domain_extractor.py
    encode_decode.py
    first_unique_char.py
    fizzbuzz.py
    group_anagrams.py
    int_to_roman.py
    is_palindrome.py
    is_rotated.py
    judge_circle.py
    knuth_morris_pratt.py
    license_number.py
    longest_common_prefix.py
    longest_palindromic_substring.py
    … 23 more files
  tree/  (42 files)
    __init__.py
    bin_tree_to_list.py
    binary_tree_paths.py
    binary_tree_views.py
    bst_array_to_bst.py
    bst_closest_value.py
    bst_count_left_node.py
    bst_delete_node.py
    bst_depth_sum.py
    bst_height.py
    bst_is_bst.py
    bst_iterator.py
    bst_kth_smallest.py
    bst_lowest_common_ancestor.py
    bst_num_empty.py
    bst_predecessor.py
    bst_serialize_deserialize.py
    bst_successor.py
    bst_unique_bst.py
    bst_validate_bst.py
    construct_tree_postorder_preorder.py
    deepest_left.py
    invert_tree.py
    is_balanced.py
    … 18 more files
  __init__.py
  py.typed
docs/  (1 files)
  index.html
tests/  (28 files)
  test_array.py
  test_audit_regressions.py
  test_backtracking.py
  test_bit_manipulation.py
  test_community_algorithms.py
  test_compression.py
  test_data_structures.py
  test_dynamic_programming.py
  test_graph.py
  test_greedy.py
  test_heap.py
  test_issue_fixes.py
  test_iterative_segment_tree.py
  test_linked_list.py
  test_map.py
  test_math.py
  test_matrix.py
  test_monomial.py
  test_polynomial.py
  test_queue.py
  test_searching.py
  test_set.py
  test_sorting.py
  test_stack.py
  … 4 more files
.gitignore
CODE_OF_CONDUCT.md
CONTRIBUTING.md
LICENSE
MANIFEST.in
README.md
pyproject.toml
```

## Entry points

- [algorithms/data_structures/red_black_tree.py:287](https://github.com/keon/algorithms/blob/bd1d152f9ec7331c69be662831610b003b10fc7a/algorithms/data_structures/red_black_tree.py#L287)
- [algorithms/searching/generalized_binary_search.py:62](https://github.com/keon/algorithms/blob/bd1d152f9ec7331c69be662831610b003b10fc7a/algorithms/searching/generalized_binary_search.py#L62)
- [algorithms/searching/interpolation_search.py:54](https://github.com/keon/algorithms/blob/bd1d152f9ec7331c69be662831610b003b10fc7a/algorithms/searching/interpolation_search.py#L54)
- [algorithms/tree/bst_count_left_node.py:65](https://github.com/keon/algorithms/blob/bd1d152f9ec7331c69be662831610b003b10fc7a/algorithms/tree/bst_count_left_node.py#L65)
- [algorithms/tree/bst_depth_sum.py:75](https://github.com/keon/algorithms/blob/bd1d152f9ec7331c69be662831610b003b10fc7a/algorithms/tree/bst_depth_sum.py#L75)
- [algorithms/tree/bst_height.py:64](https://github.com/keon/algorithms/blob/bd1d152f9ec7331c69be662831610b003b10fc7a/algorithms/tree/bst_height.py#L64)
- [algorithms/tree/bst_kth_smallest.py:42](https://github.com/keon/algorithms/blob/bd1d152f9ec7331c69be662831610b003b10fc7a/algorithms/tree/bst_kth_smallest.py#L42)
- [algorithms/tree/bst_num_empty.py:71](https://github.com/keon/algorithms/blob/bd1d152f9ec7331c69be662831610b003b10fc7a/algorithms/tree/bst_num_empty.py#L71)
- [algorithms/tree/bst_validate_bst.py:71](https://github.com/keon/algorithms/blob/bd1d152f9ec7331c69be662831610b003b10fc7a/algorithms/tree/bst_validate_bst.py#L71)
- [algorithms/tree/traversal_inorder.py:41](https://github.com/keon/algorithms/blob/bd1d152f9ec7331c69be662831610b003b10fc7a/algorithms/tree/traversal_inorder.py#L41)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| algorithms package | library | Observed | Groups 395 file(s) under algorithms package (observed from repository paths and static analysis). Observed top-level classes: AbstractHeap, AbstractQueue, AbstractStack, ArrayQueue, ArrayStack, AvlTree. Observed top-lev… |
| Configuration and deployment | config | Observed | Groups 2 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 10 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: Node, RBNode, RBTree, Solution, TestSuite. Observed top-level functions: binary_search_fi… |
| Tests | test | Observed | Groups 28 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: Node, PrimsMinimumSpanning, TestAddBinary, TestAddOperator, TestAllFactors, TestAllPairsShortestPath. Obser… |

## Important files

- `.github/workflows/publish.yml` (ci)
- `.github/workflows/python-app.yml` (ci)
- `MANIFEST.in` (manifest)
- `pyproject.toml` (manifest)

## Top-level layout

- `algorithms` — 406 analysed file(s)
- `tests` — 28 analysed file(s)
- `(root files)` — 7 analysed file(s)
- `.github` — 2 analysed file(s)
- `docs` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `bd1d152f9ec7331c69be662831610b003b10fc7a` is the revision these paths and observations refer to.
