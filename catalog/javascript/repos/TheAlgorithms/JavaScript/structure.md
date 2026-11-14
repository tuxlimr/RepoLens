# Project structure: TheAlgorithms/JavaScript

**Analysed commit:** `5c39e87a9a31f279c60f830ad74a845e4788a517`

**Commit reference:** [5c39e87a9a31f279c60f830ad74a845e4788a517](https://github.com/TheAlgorithms/JavaScript/commit/5c39e87a9a31f279c60f830ad74a845e4788a517)

**Tree at this commit:** [TheAlgorithms/JavaScript@5c39e87a9a31](https://github.com/TheAlgorithms/JavaScript/tree/5c39e87a9a31f279c60f830ad74a845e4788a517)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | TheAlgorithms/JavaScript |
| Description | Algorithms and Data Structures implemented in JavaScript for beginners, following best practices. |
| Stars | 34276 |
| Forks | 5824 |
| Licence | GPL-3.0 |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `5c39e87a9a31f279c60f830ad74a845e4788a517` |
| Retrieved at | 2026-11-14T19:10:43.616717+00:00 |
| Files in this snapshot | 751 |

## Directory tree

```text
.github/  (12 files)
  ISSUE_TEMPLATE/  (4 files)
    bug_report.yml
    config.yml
    feature_request.yml
    other.yml
  workflows/  (4 files)
    Ci.yml
    UpdateDirectory.js
    UpdateDirectory.yml
    UploadCoverageReport.yml
  CODEOWNERS
  dependabot.yml
  pull_request_template.md
  stale.yml
.husky/  (1 files)
  pre-commit
Backtracking/  (18 files)
  tests/  (9 files)
    AllCombinationsOfSizeK.test.js
    GenerateParentheses.test.js
    GeneratePermutations.test.js
    KnightTour.test.js
    MColoringProblem.test.js
    NQueens.test.js
    RatInAMaze.test.js
    Sudoku.test.js
    SumOfSubset.test.js
  AllCombinationsOfSizeK.js
  GeneratePermutations.js
  KnightTour.js
  MColoringProblem.js
  NQueens.js
  RatInAMaze.js
  Sudoku.js
  SumOfSubset.js
  generateParentheses.js
Bit-Manipulation/  (18 files)
  test/  (9 files)
    BinaryCountSetBits.test.js
    GenerateSubSets.test.js
    GrayCodes.test.js
    IsPowerOfFour.test.js
    IsPowerOfTwo.test.js
    LogTwo.test.js
    NextPowerOfTwo.test.js
    SetBit.test.js
    UniqueElementInAnArray.test.js
  BinaryCountSetBits.js
  GenerateSubSets.js
  GrayCodes.js
  IsPowerOfTwo.js
  IsPowerofFour.js
  LogTwo.js
  NextPowerOfTwo.js
  SetBit.js
  UniqueElementInAnArray.js
Cache/  (7 files)
  test/  (4 files)
    LFUCache.test.js
    LRUCache.test.js
    Memoize.test.js
    cacheTest.js
  LFUCache.js
  LRUCache.js
  Memoize.js
Cellular-Automata/  (4 files)
  test/  (2 files)
    ConwaysGameOfLife.test.js
    Elementary.test.js
  ConwaysGameOfLife.js
  Elementary.js
Ciphers/  (17 files)
  test/  (8 files)
    AffineCipher.test.js
    Atbash.test.js
    CaesarCipher.test.js
    KeywordShiftedAlphabet.test.js
    MorseCode.test.js
    ROT13.test.js
    VigenereCipher.test.js
    XORCipher.test.js
  AffineCipher.js
  Atbash.js
  CaesarCipher.js
  KeyFinder.js
  KeywordShiftedAlphabet.js
  MorseCode.js
  ROT13.js
  VigenereCipher.js
  XORCipher.js
Compression/  (2 files)
  test/  (1 files)
    RLE.test.js
  RLE.js
Conversions/  (58 files)
  test/  (29 files)
    ArbitraryBase.test.js
    ArrayBufferToBase64.test.js
    Base64ToArrayBuffer.test.js
    BinaryToDecimal.test.js
    BinaryToHex.test.js
    DateDayDiffernce.test.js
    DateToDay.test.js
    DecimalToBinary.test.js
    DecimalToHex.test.js
    DecimalToOctal.test.js
    DecimalToRoman.test.js
    HexToBinary.test.js
    HexToDecimal.test.js
    HexToRGB.test.js
    LengthConversion.test.js
    LitersToImperialGallons.test.js
    LitersToUSGallons.test.js
    LowerCaseConversion.test.js
    MeterToFeetConversion.test.js
    OctToDecimal.test.js
    OuncesToKilogram.test.js
    RGBToHex.test.js
    RailwayTimeConversion.test.js
    RgbHslConversion.test.js
    … 5 more files
  ArbitraryBase.js
  ArrayBufferToBase64.js
  Base64ToArrayBuffer.js
  BinaryToDecimal.js
  BinaryToHex.js
  DateDayDifference.js
  DateToDay.js
  DecimalToBinary.js
  DecimalToHex.js
  DecimalToOctal.js
  DecimalToRoman.js
  HexToBinary.js
  HexToDecimal.js
  HexToRGB.js
  LengthConversion.js
  LitersToImperialGallons.js
  LitersToUSGallons.js
  LowerCaseConversion.js
  MeterToFeetConversion.js
  OctToDecimal.js
  OuncesToKilograms.js
  RGBToHex.js
  RailwayTimeConversion.js
  RgbHslConversion.js
  … 5 more files
Data-Structures/  (53 files)
  Array/  (8 files)
    test/  (4 files)
      … 4 files under this directory
    LocalMaximumPoint.js
    NumberOfLocalMaximumPoints.js
    QuickSelect.js
    Reverse.js
  Graph/  (5 files)
    test/  (2 files)
      … 2 files under this directory
    Graph.js
    Graph2.js
    Graph3.js
  Heap/  (6 files)
    test/  (3 files)
      … 3 files under this directory
    BinaryHeap.js
    KeyPriorityQueue.js
    MinPriorityQueue.js
  Linked-List/  (16 files)
    test/  (8 files)
      … 8 files under this directory
    AddTwoNumbers.js
    CycleDetection.js
    CycleDetectionII.js
    DoublyLinkedList.js
    MergeTwoSortedLinkedLists.js
    ReverseSinglyLinkedList.js
    SinglyCircularLinkedList.js
    SinglyLinkedList.js
  Queue/  (5 files)
    test/  (2 files)
      … 2 files under this directory
    CircularQueue.js
    Queue.js
    QueueUsing2Stacks.js
  Stack/  (4 files)
    test/  (1 files)
      … 1 files under this directory
    EvaluateExpression.js
    Stack.js
    StackES6.js
  Tree/  (7 files)
    test/  (3 files)
      … 3 files under this directory
    AVLTree.js
    BinarySearchTree.js
    SegmentTree.js
    Trie.js
  Vectors/  (2 files)
    test/  (1 files)
      … 1 files under this directory
    Vector2.js
Dynamic-Programming/  (59 files)
  Sliding-Window/  (10 files)
    test/  (5 files)
      … 5 files under this directory
    HouseRobber.js
    LongestSubstringWithoutRepeatingCharacters.js
    MaxConsecutiveOnes.js
    MaxConsecutiveOnesIII.js
    PermutationinString.js
  tests/  (22 files)
    Abbreviation.test.js
    CatalanNumbers.test.js
    ClimbingStairs.test.js
    CoinChange.test.js
    EditDistance.test.js
    FastFibonacciNumber.test.js
    FibonacciNumber.test.js
    KadaneAlgo.test.js
    LevenshteinDistance.test.js
    LongestCommonSubsequence.test.js
    LongestIncreasingSubsequence.test.js
    LongestPalindromicSubsequence.test.js
    LongestValidParentheses.test.js
    MaxProductOfThree.test.js
    NumberOfSubsetEqualToGivenSum.test.js
    RodCutting.test.js
    SieveOfEratosthenes.test.js
    TrappingRainWater.test.js
    TribonacciNumber.test.js
    UniquePaths.test.js
    UniquePaths2.test.js
    ZeroOneKnapsack.test.js
  Abbreviation.js
  CatalanNumbers.js
  ClimbingStairs.js
  CoinChange.js
  EditDistance.js
  FastFibonacciNumber.js
  FibonacciNumber.js
  FindMonthCalendar.js
  KadaneAlgo.js
  LevenshteinDistance.js
  LongestCommonSubsequence.js
  LongestIncreasingSubsequence.js
  LongestPalindromicSubsequence.js
  LongestValidParentheses.js
  MaxNonAdjacentSum.js
  MaxProductOfThree.js
  MinimumCostPath.js
  NumberOfSubsetEqualToGivenSum.js
  RodCutting.js
  Shuf.js
  SieveOfEratosthenes.js
  SudokuSolver.js
  TrappingRainWater.js
  TribonacciNumber.js
  … 3 more files
Geometry/  (10 files)
  Test/  (5 files)
    Circle.test.js
    Cone.test.js
    ConvexHullGraham.test.js
    Pyramid.test.js
    Sphere.test.js
  Circle.js
  Cone.js
  ConvexHullGraham.js
  Pyramid.js
  Sphere.js
Graphs/  (25 files)
  test/  (8 files)
    BellmanFord.test.js
    BinaryLifting.test.js
    BreadthFirstSearch.test.js
    BreadthFirstShortestPath.test.js
    Kosaraju.test.js
    LCABinaryLifting.test.js
    NumberOfIslands.test.js
    PrimMST.test.js
  BellmanFord.js
  BinaryLifting.js
  BreadthFirstSearch.js
  BreadthFirstShortestPath.js
  ConnectedComponents.js
  Density.js
  DepthFirstSearchIterative.js
  DepthFirstSearchRecursive.js
  Dijkstra.js
  DijkstraSmallestPath.js
  FloydWarshall.js
  Kosaraju.js
  KruskalMST.js
  LCABinaryLifting.js
  NodeNeighbors.js
  NumberOfIslands.js
  PrimMST.js
Hashes/  (6 files)
  tests/  (3 files)
    MD5.test.js
    SHA1.test.js
    SHA256.test.js
  MD5.js
  SHA1.js
  SHA256.js
Maths/  (192 files)
  test/  (95 files)
    Abs.test.js
    AliquotSum.test.js
    Area.test.js
    ArithmeticGeometricMean.test.js
    ArmstrongNumber.test.js
    AutomorphicNumber.test.js
    AverageMean.test.js
    AverageMedian.test.js
    BInaryConvert.test.js
    BinaryExponentiationIterative.test.js
    BinaryExponentiationRecursive.test.js
    BinomialCoefficient.test.js
    BisectionMethod.test.js
    CheckKishnamurthyNumber.test.js
    CircularArc.test.js
    CoPrimeCheck.test.js
    CollatzSequence.test.js
    Coordinate.test.js
    CountNumbersDivisible.test.js
    DecimalExpansion.test.js
    DegreeToRadian.test.js
    Determinant.test.js
    EuclideanDistance.test.js
    EulerMethod.manual-test.js
    … 71 more files
  Abs.js
  AliquotSum.js
  Area.js
  ArithmeticGeometricMean.js
  ArmstrongNumber.js
  AutomorphicNumber.js
  AverageMean.js
  AverageMedian.js
  BinaryConvert.js
  BinaryExponentiationIterative.js
  BinaryExponentiationRecursive.js
  BinomialCoefficient.js
  BisectionMethod.js
  CheckKishnamurthyNumber.js
  CircularArc.js
  CoPrimeCheck.js
  CollatzSequence.js
  Coordinate.js
  CountNumbersDivisible.js
  DecimalExpansion.js
  DecimalIsolate.js
  DegreeToRadian.js
  Determinant.js
  EuclideanDistance.js
  … 73 more files
Navigation/  (2 files)
  test/  (1 files)
    Haversine.test.js
  Haversine.js
Project-Euler/  (51 files)
  test/  (25 files)
    Problem001.test.js
    Problem002.test.js
    Problem003.test.js
    Problem004.test.js
    Problem005.test.js
    Problem006.test.js
    Problem007.test.js
    Problem008.test.js
    Problem009.test.js
    Problem010.test.js
    Problem011.test.js
    Problem012.test.js
    Problem013.test.js
    Problem014.test.js
    Problem016.test.js
    Problem017.test.js
    Problem018.test.js
    Problem019.test.js
    Problem020.test.js
    Problem021.test.js
    Problem023.test.js
    Problem025.test.js
    Problem028.test.js
    Problem035.test.js
    … 1 more files
  Problem001.js
  Problem002.js
  Problem003.js
  Problem004.js
  Problem005.js
  Problem006.js
  Problem007.js
  Problem008.js
  Problem009.js
  Problem010.js
  Problem011.js
  Problem012.js
  Problem013.js
  Problem014.js
  Problem015.js
  Problem016.js
  Problem017.js
  Problem018.js
  Problem019.js
  Problem020.js
  Problem021.js
  Problem023.js
  Problem025.js
  Problem028.js
  … 2 more files
Recursive/  (23 files)
  test/  (10 files)
    BinaryEquivalent.test.js
    BinarySearch.test.js
    Factorial.test.js
    FibonacciNumberRecursive.test.js
    FloodFill.test.js
    KochSnowflake.test.js
    LetterCombination.test.js
    Palindrome.test.js
    PalindromePartitioning.test.js
    Partition.test.js
  BinaryEquivalent.js
  BinarySearch.js
  Factorial.js
  FibonacciNumberRecursive.js
  FloodFill.js
  KochSnowflake.js
  KochSnowflake.manual-test.js
  LetterCombination.js
  Palindrome.js
  PalindromePartitioning.js
  Partition.js
  SubsequenceRecursive.js
  TowerOfHanoi.js
Search/  (24 files)
  test/  (11 files)
    BinarySearch.test.js
    ExponentialSearch.test.js
    FibonacciSearch.test.js
    InterpolationSearch.test.js
    LinearSearch.test.js
    Minesweeper.test.js
    RabinKarp.test.js
    SlidingWindow.test.js
    TernarySearch.test.js
    UnionFind.test.js
    jumpSearch.test.js
  BinarySearch.js
  ExponentialSearch.js
  FibonacciSearch.js
  InterpolationSearch.js
  JumpSearch.js
  LinearSearch.js
  Minesweeper.js
  QuickSelectSearch.js
  RabinKarp.js
  SlidingWindow.js
  StringSearch.js
  TernarySearch.js
  UnionFind.js
Sliding-Windows/  (4 files)
  test/  (2 files)
    LongestSubarrayWithSumAtMost.test.js
    MaxSumSubarrayFixed.test.js
  LongestSubarrayWithSumAtMost.js
  MaxSumSubarrayFixed.js
Sorts/  (65 files)
  test/  (32 files)
    AlphaNumericalSort.test.js
    BeadSort.test.js
    BinaryInsertionSort.test.js
    BogoSort.test.js
    BubbleSort.test.js
    BucketSort.test.js
    CocktailShakerSort.test.js
    CombSort.test.js
    CountingSort.test.js
    CycleSort.test.js
    DutchNationalFlagSort.test.js
    FindSecondLargestElement.test.js
    FisherYatesShuffle.test.js
    FlashSort.test.js
    GnomeSort.test.js
    HeapSort.test.js
    HeapSortV2.test.js
    InsertionSort.test.js
    MergeSort.test.js
    OddEvenSort.test.js
    PancakeSort.test.js
    PigeonHoleSort.test.js
    QuickSort.test.js
    QuickSortRecursive.test.js
    … 8 more files
  AlphaNumericalSort.js
  BeadSort.js
  BinaryInsertionSort.js
  BogoSort.js
  BubbleSort.js
  BucketSort.js
  CocktailShakerSort.js
  CombSort.js
  CountingSort.js
  CycleSort.js
  DutchNationalFlagSort.js
  FindSecondLargestElement.js
  FisherYatesShuffle.js
  FlashSort.js
  GnomeSort.js
  HeapSort.js
  HeapSortV2.js
  InsertionSort.js
  IntroSort.js
  MergeSort.js
  OddEvenSort.js
  PancakeSort.js
  PigeonHoleSort.js
  QuickSort.js
  … 9 more files
String/  (79 files)
  test/  (39 files)
    AlphaNumericPalindrome.test.js
    AlternativeStringArrange.test.js
    BoyerMoore.test.js
    CheckAnagram.test.js
    CheckCamelCase.test.js
    CheckExceeding.test.js
    CheckFlatCase.test.js
    CheckKebabCase.test.js
    CheckPalindrome.test.js
    CheckPangram.test.js
    CheckPascalCase.test.js
    CheckRearrangePalindrome.test.js
    CheckSnakeCase.test.js
    CheckWordOcurrence.test.js
    CountLetters.test.js
    CountSubstrings.test.js
    CountVowels.test.js
    CreatePermutations.test.js
    DiceCoefficient.test.js
    FirstUniqueCharacter.test.js
    FormatPhoneNumber.test.js
    HammingDistance.test.js
    IsPalindrome.test.js
    KMPPatternSearching.test.js
    … 15 more files
  AlphaNumericPalindrome.js
  AlternativeStringArrange.js
  BoyerMoore.js
  CheckAnagram.js
  CheckCamelCase.js
  CheckExceeding.js
  CheckFlatCase.js
  CheckKebabCase.js
  CheckPalindrome.js
  CheckPangram.js
  CheckPascalCase.js
  CheckRearrangePalindrome.js
  CheckSnakeCase.js
  CheckWordOccurrence.js
  CountLetters.js
  CountSubstrings.js
  CountVowels.js
  CreatePermutations.js
  DiceCoefficient.js
  FirstUniqueCharacter.js
  FormatPhoneNumber.js
  GenerateGUID.js
  HammingDistance.js
  IsPalindrome.js
  … 16 more files
Timing-Functions/  (5 files)
  test/  (2 files)
    GetMonthDays.test.js
    ParseDate.test.js
  GetMonthDays.js
  IntervalTimer.js
  ParseDate.js
Trees/  (6 files)
  test/  (3 files)
    BreadthFirstTreeTraversal.test.js
    DepthFirstSearch.test.js
    FenwickTree.test.js
  BreadthFirstTreeTraversal.js
  DepthFirstSearch.js
  FenwickTree.js
.gitignore
.gitpod.yml
.prettierignore
.prettierrc
CONTRIBUTING.md
DIRECTORY.md
LICENSE
README.md
package.json
vitest.config.ts
```

## Entry points

No application entry point was observed at this commit.

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Backtracking package | library | Observed | Groups 9 file(s) under backtracking package (observed from repository paths and static analysis). |
| Bit-Manipulation package | library | Observed | Groups 9 file(s) under bit-manipulation package (observed from repository paths and static analysis). |
| Cache package | library | Observed | Groups 3 file(s) under cache package (observed from repository paths and static analysis). |
| Cellular-Automata package | library | Observed | Groups 2 file(s) under cellular-automata package (observed from repository paths and static analysis). |
| Ciphers package | library | Observed | Groups 9 file(s) under ciphers package (observed from repository paths and static analysis). |
| Compression package | library | Observed | Groups 1 file(s) under compression package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 1 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Conversions package | library | Observed | Groups 29 file(s) under conversions package (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| Data-Structures package | library | Observed | Groups 29 file(s) under data-structures package (observed from repository paths and static analysis). |
| Dynamic-Programming package | library | Observed | Groups 32 file(s) under dynamic-programming package (observed from repository paths and static analysis). |
| Geometry package | library | Observed | Groups 5 file(s) under geometry package (observed from repository paths and static analysis). |
| Graphs package | library | Observed | Groups 17 file(s) under graphs package (observed from repository paths and static analysis). |
| Hashes package | library | Observed | Groups 3 file(s) under hashes package (observed from repository paths and static analysis). |
| Maths package | library | Observed | Groups 97 file(s) under maths package (observed from repository paths and static analysis). |
| Navigation package | library | Observed | Groups 1 file(s) under navigation package (observed from repository paths and static analysis). |
| Project-Euler package | library | Observed | Groups 26 file(s) under project-euler package (observed from repository paths and static analysis). |
| Recursive package | library | Observed | Groups 13 file(s) under recursive package (observed from repository paths and static analysis). |
| Search package | library | Observed | Groups 13 file(s) under search package (observed from repository paths and static analysis). |
| Sliding-Windows package | library | Observed | Groups 2 file(s) under sliding-windows package (observed from repository paths and static analysis). |
| Sorts package | library | Observed | Groups 33 file(s) under sorts package (observed from repository paths and static analysis). |
| String package | library | Observed | Groups 40 file(s) under string package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 349 file(s) under tests (observed from repository paths and static analysis). |
| Timing-Functions package | library | Observed | Groups 3 file(s) under timing-functions package (observed from repository paths and static analysis). |
| Trees package | library | Observed | Groups 3 file(s) under trees package (observed from repository paths and static analysis). |

## Important files

- `.github/ISSUE_TEMPLATE/bug_report.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/ISSUE_TEMPLATE/feature_request.yml` (config)
- `.github/ISSUE_TEMPLATE/other.yml` (config)
- `.github/dependabot.yml` (config)
- `.github/stale.yml` (config)
- `.github/workflows/Ci.yml` (ci)
- `.github/workflows/UpdateDirectory.js` (ci)
- `.github/workflows/UpdateDirectory.yml` (ci)
- `.github/workflows/UploadCoverageReport.yml` (ci)
- `.gitpod.yml` (config)
- `package.json` (manifest)

## Top-level layout

- `Maths` — 192 analysed file(s)
- `String` — 79 analysed file(s)
- `Sorts` — 65 analysed file(s)
- `Dynamic-Programming` — 59 analysed file(s)
- `Conversions` — 58 analysed file(s)
- `Data-Structures` — 53 analysed file(s)
- `Project-Euler` — 51 analysed file(s)
- `Graphs` — 25 analysed file(s)
- `Search` — 24 analysed file(s)
- `Recursive` — 23 analysed file(s)
- `Backtracking` — 18 analysed file(s)
- `Bit-Manipulation` — 18 analysed file(s)
- `Ciphers` — 17 analysed file(s)
- `.github` — 12 analysed file(s)
- `(root files)` — 10 analysed file(s)
- `Geometry` — 10 analysed file(s)
- `Cache` — 7 analysed file(s)
- `Hashes` — 6 analysed file(s)
- `Trees` — 6 analysed file(s)
- `Timing-Functions` — 5 analysed file(s)
- `Cellular-Automata` — 4 analysed file(s)
- `Sliding-Windows` — 4 analysed file(s)
- `Compression` — 2 analysed file(s)
- `Navigation` — 2 analysed file(s)
- `.husky` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `5c39e87a9a31f279c60f830ad74a845e4788a517` is the revision these paths and observations refer to.
