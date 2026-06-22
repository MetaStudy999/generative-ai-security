# W03 Experiment Run Log

- week: W03
- topic: 컴퓨터비전 표현학습 & 비전 대적공격
- dataset: synthetic_8x8_bar_images
- seed: 42
- model: nearest_centroid
- run_at_utc: 2026-06-22T12:57:53.833889+00:00
- safety_scope: {'allowed': 'toy evaluation and literature-based risk analysis', 'disallowed': 'actual system compromise, personal data use, unauthorized attack'}

## Metrics

| Condition | Epsilon | Defense | N | Accuracy | Macro F1 | ASR | Robust Drop |
|---|---:|---|---:|---:|---:|---:|---:|
| clean_baseline | 0.00 | none | 120 | 1.000000 | 1.000000 |  | 0.000000 |
| centroid_direction_linf | 0.05 | none | 120 | 1.000000 | 1.000000 | 0.000000 | 0.000000 |
| centroid_direction_linf | 0.15 | none | 120 | 1.000000 | 1.000000 | 0.000000 | 0.000000 |
| centroid_direction_linf | 0.30 | none | 120 | 1.000000 | 1.000000 | 0.000000 | 0.000000 |
| centroid_direction_linf | 0.45 | none | 120 | 0.000000 | 0.000000 | 1.000000 | 1.000000 |
| adversarial_with_feature_squeeze | 0.30 | feature_squeeze_2_levels | 120 | 1.000000 | 1.000000 | 0.000000 | 0.000000 |

## Confusion Matrices

Rows are true labels and columns are predicted labels.

### clean_baseline eps=0.00 defense=none

[[60, 0], [0, 60]]

### centroid_direction_linf eps=0.05 defense=none

[[60, 0], [0, 60]]

### centroid_direction_linf eps=0.15 defense=none

[[60, 0], [0, 60]]

### centroid_direction_linf eps=0.30 defense=none

[[60, 0], [0, 60]]

### centroid_direction_linf eps=0.45 defense=none

[[0, 60], [60, 0]]

### adversarial_with_feature_squeeze eps=0.30 defense=feature_squeeze_2_levels

[[60, 0], [0, 60]]

