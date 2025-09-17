CREATE TABLE `EvaTextML` (
  `id` int NOT NULL AUTO_INCREMENT,
  `thetext` text,
  `label` text,
  `dstype` text,
  `labeltype` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17482 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Insert the existing testing datasets
INSERT INTO `myresearch`.`EvaTextML`(`id`,`thetext`,`label`,`dstype`,`labeltype`)
select id, thetext, label, dstype, labeltype from EvaText;

-- Add columns for models
alter table EvaTextML add DecisionTreeClassifier_lbl text;
alter table EvaTextML add KNeighborsClassifier_lbl text;
alter table EvaTextML add LinearSVC_lbl text;
alter table EvaTextML add LogisticRegression_lbl text;
alter table EvaTextML add MultinomialNB_lbl text;
alter table EvaTextML add RandomForestClassifier_lbl text;
alter table EvaTextML add DecisionTreeClassifierGPT_lbl text;
alter table EvaTextML add KNeighborsClassifierGPT_lbl text;
alter table EvaTextML add LinearSVCGPT_lbl text;
alter table EvaTextML add LogisticRegressionGPT_lbl text;
alter table EvaTextML add MultinomialNBGPT_lbl text;
alter table EvaTextML add RandomForestClassifierGPT_lbl text;

alter table EvaTextML add DecisionTreeClassifier_plbl text;
alter table EvaTextML add KNeighborsClassifier_plbl text;
alter table EvaTextML add LinearSVC_plbl text;
alter table EvaTextML add LogisticRegression_plbl text;
alter table EvaTextML add MultinomialNB_plbl text;
alter table EvaTextML add RandomForestClassifier_plbl text;
alter table EvaTextML add DecisionTreeClassifierGPT_plbl text;
alter table EvaTextML add KNeighborsClassifierGPT_plbl text;
alter table EvaTextML add LinearSVCGPT_plbl text;
alter table EvaTextML add LogisticRegressionGPT_plbl text;
alter table EvaTextML add MultinomialNBGPT_plbl text;
alter table EvaTextML add RandomForestClassifierGPT_plbl text;

alter table EvaTextML add DecisionTreeClassifier_slbl text;
alter table EvaTextML add KNeighborsClassifier_slbl text;
alter table EvaTextML add LinearSVC_slbl text;
alter table EvaTextML add LogisticRegression_slbl text;
alter table EvaTextML add MultinomialNB_slbl text;
alter table EvaTextML add RandomForestClassifier_slbl text;
alter table EvaTextML add DecisionTreeClassifierGPT_slbl text;
alter table EvaTextML add KNeighborsClassifierGPT_slbl text;
alter table EvaTextML add LinearSVCGPT_slbl text;
alter table EvaTextML add LogisticRegressionGPT_slbl text;
alter table EvaTextML add MultinomialNBGPT_slbl text;
alter table EvaTextML add RandomForestClassifierGPT_slbl text;

select id, thetext, label, dstype, labeltype from EvaTextML where DecisionTreeClassifier_lbl is null

select count(1) from EvaTextML where DecisionTreeClassifier_lbl is null



