# Machine learning FAQs


***Q: What's the difference between supervised and unsupervised learning?***

Supervised learning uses labeled examples to train models to map inputs to outputs. Common tasks include classification and regression. Unsupervised learning finds hidden patterns and structures in unlabeled data through clustering, dimensionality reduction, etc. No labels are given for the outputs.

***Q: How do I choose the right predictive model for my supervised learning problem?***

Consider your problem (classification vs. regression), the number of predictors, scales of measurement, and whether relationships are assumed to be linear. Common options include linear/logistic regression, decision trees, nearest neighbors, SVM, and neural networks. Test several on your data and evaluate error rates through cross-validation.

***Q: How do I select features for my machine-learning models?***

Remove uninformative features through domain knowledge, correlation analysis, or filtering out near-zero variance. Use regularization like L1 penalty for sparsity or L2 for grouping related features. Evaluate and compare the performance of recursive feature elimination or automated feature selection techniques.

***Q: What evaluation metrics should I use for classification and regression problems?***

A: For classification, use accuracy, precision, recall, and the F1 score. For imbalanced classes, also consider the ROC AUC. For regression, use R^2, RMSE, and MAE. Some tasks also use log loss or Brier scores. Compare to benchmark/null models. Validate held-out data with cross-validation as well.

***Q: What's the best way to optimize hyperparameters for my models?***

Do a random/grid search on a small subset of values to identify promising areas. Then use Bayesian optimization, which iteratively explores the next best configuration based on priors, to efficiently search a larger space. Track results through cross-validation to select the configuration with the best performance.

***Q: How can I handle missing data in my analysis?***

 Depending on the nature and extent of missingness, techniques such as complete case analysis, imputation methods (e.g., mean imputation, multiple imputation), or advanced algorithms like expectation-maximization (EM) can be used. The choice of method should be based on the underlying assumptions and potential biases introduced by each approach.

***Q: What are some techniques for dimensionality reduction in machine learning?***

Techniques for dimensionality reduction include Principal Component Analysis (PCA), Linear Discriminant Analysis (LDA), t-SNE (t-distributed Stochastic Neighbor Embedding), and Autoencoders. These techniques help reduce the number of features in the data while preserving relevant information.
