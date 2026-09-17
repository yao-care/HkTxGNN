---
layout: default
title: Pantothenic Acid
parent: 僅模型預測 (L5)
nav_order: 560
evidence_level: L5
indication_count: 5
---

# Pantothenic Acid
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Pantothenic Acid（泛酸）：老藥新用候選適應症評估

## 一句話總結

Pantothenic acid（泛酸，維生素 B5，DrugBank ID: DB01783）目前在香港未上市，且原始核准適應症與作用機轉資料皆缺失。TxGNN 模型針對此藥物產出 **5 個候選適應症**，其中僅「**葉酸缺乏性貧血**」證據相對完整（4 個臨床試驗、4 篇文獻，已達 S1 決策階段），其餘 4 個候選證據等級偏低（L4-L5），多屬間接機轉推測或雜訊配對，建議 Hold。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 尚無資料（泛酸為維生素補充品，本評估包未提供正式核准適應症） |
| 作用機轉 (MOA) | 尚無資料 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 候選新適應症數 | 5 個 |
| 最佳候選 | 葉酸缺乏性貧血 (folic acid deficiency anemia)，L3／S1／Research Question |
| 整體建議決策 | Hold（單一候選「葉酸缺乏性貧血」可列為 Research Question） |

### 五個候選適應症總覽

| 排名 | 候選適應症 | TxGNN 分數 | 全域排名 | 證據等級 | 決策階段 | 建議 |
|------|-----------|-----------|---------|---------|---------|------|
| 1 | 先天性凝血酶原缺乏症 (congenital prothrombin deficiency) | 99.96% | 1158 | L5 | S0 | Hold |
| 2 | 褐黃病 (ochronosis disorder) | 99.78% | 5016 | L5 | S0 | Hold |
| 3 | 甘油代謝疾病 (glycerol metabolism disease) | 99.77% | 5062 | L4 | S0 | Hold |
| 4 | 葉酸缺乏性貧血 (folic acid deficiency anemia) | 99.60% | 7749 | L3 | S1 | Research Question |
| 5 | 子宮發炎性疾病 (uterine inflammatory disease) | 99.14% | 13706 | L4 | S0 | Hold |

> 說明：TxGNN 分數本身普遍偏高（>99%），實際參考價值需搭配全域排名與證據來源判讀——排名數字越小代表在所有預測中相對信心越高。

---

## 候選適應症逐一分析

### 1. 葉酸缺乏性貧血（folic acid deficiency anemia）— 最具潛力

**機轉推論：** 泛酸為輔酶 A (CoA) 合成前驅物，B 群維生素在營養不良狀態下常合併缺乏（含葉酸），CoA 依賴之紅血球生成路徑理論上可能受影響。但現有證據多來自多重營養素強化介入（非泛酸單一成分），因果特異性較弱；1946 年舊文獻雖直接提及泛酸/葉酸缺乏與貧血的關聯，但方法學證據等級低。

**臨床試驗證據**

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT06425796](https://clinicaltrials.gov/study/NCT06425796) | NA | 招募中 | 312 | 探討孕期體脂對鐵狀態與需求之影響，未直接測試泛酸 |
| [NCT03444155](https://clinicaltrials.gov/study/NCT03444155) | NA | 完成 | 30 | 天然 vs 合成維生素 B 群先導研究，涵蓋泛酸但樣本數小 |
| [NCT03891589](https://clinicaltrials.gov/study/NCT03891589) | NA | 完成 | 215 | 家庭強化副食品(Taburia)預防五歲以下兒童貧血之介入試驗 |
| [NCT02567981](https://clinicaltrials.gov/study/NCT02567981) | NA | 未知 | 4577 | 強化預混粉之社區介入，多重營養素、特異性低 |

**文獻證據**

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [21929634](https://pubmed.ncbi.nlm.nih.gov/21929634/) | 2011 | Review | Maternal & Child Nutrition | 強化食品/飲品對孕產婦貧血與缺鐵有正向效果 |
| [23297780](https://pubmed.ncbi.nlm.nih.gov/23297780/) | 2013 | RCT (small) | J Oral Pathol Med | 維生素補充治療降低灼口症患者血清同半胱氨酸並改善口腔症狀 |
| [21021037](https://pubmed.ncbi.nlm.nih.gov/21021037/) | 1946 | Case series/Experimental | Nutrition Reviews | 直接提及泛酸與葉酸缺乏與貧血、粒細胞減少之關聯 |
| [3724048](https://pubmed.ncbi.nlm.nih.gov/3724048/) | 1986 | Animal study | Laboratory Animal Science | 回顧非人靈長類因泛酸等多種營養素缺乏誘發之貧血 |

### 2. 甘油代謝疾病（glycerol metabolism disease）— Hold

**機轉推論：** CoA 為脂肪酸酯化/甘油三酯合成之必需輔酶，泛酸缺乏理論上可能干擾甘油代謝路徑；但現有文獻皆為代謝體學觀察性研究（顯示相關代謝物濃度變化），非治療性介入證據，機轉關聯僅為間接關聯而非因果驗證。

**文獻證據**

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [35296075](https://pubmed.ncbi.nlm.nih.gov/35296075/) | 2022 | Observational/Metabolomics | Frontiers in Immunology | 乾癬性關節炎糞便代謝體異於類風濕性關節炎，可能之生物標記 |
| [20505214](https://pubmed.ncbi.nlm.nih.gov/20505214/) | 2010 | Observational/Metabolomics | Science Translational Medicine | 運動誘發之血漿代謝標記，含甘油等脂解指標 |
| [22380686](https://pubmed.ncbi.nlm.nih.gov/22380686/) | 2012 | Animal study | J Proteome Research | 老年大鼠肝臟代謝體分析，甘油-3-磷酸為區辨代謝物之一 |
| [34868045](https://pubmed.ncbi.nlm.nih.gov/34868045/) | 2021 | Animal/in vitro study | Frontiers in Immunology | Resveratrol 經腸道菌調節減緩 LPS 誘發發炎 |
| [41597540](https://pubmed.ncbi.nlm.nih.gov/41597540/) | 2025 | Animal study | Microorganisms | 二氫楊梅素補充對乳牛後腸菌相與代謝物之影響 |

無臨床試驗登記。

### 3. 子宮發炎性疾病（uterine inflammatory disease）— Hold

**機轉推論：** CoA 依賴之能量代謝與組織修復機轉可能參與子宮內膜損傷修復；唯一支持證據為 2026 年單一小鼠模型（迷走神經切斷誘發之內膜損傷），尚無人體或其他物種驗證，機轉推論屬初步階段。

**文獻證據**

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [41223999](https://pubmed.ncbi.nlm.nih.gov/41223999/) | 2026 | Animal study | Mucosal Immunology | 泛酸緩解小鼠迷走神經切斷誘發之子宮內膜損傷 |

無臨床試驗登記。

### 4. 先天性凝血酶原缺乏症（congenital prothrombin deficiency）— Hold，疑似雜訊配對

**機轉推論：** 泛酸/CoA 路徑與凝血因子 II（prothrombin）合成無已知經典機轉關聯（凝血因子合成主要依賴維生素 K）。唯一配對的試驗實際研究主題為內皮功能與輕中度高血壓，與此適應症無關，判定為 TxGNN 預測雜訊/偽陽性配對。

**臨床試驗證據**

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT02392767](https://clinicaltrials.gov/study/NCT02392767) | NA | 完成 | 25 | 膳食補充品對高血壓志願者內皮功能之影響（與本適應症無實質關聯，屬錯誤配對） |

### 5. 褐黃病（ochronosis disorder）— Hold，無支持證據

**機轉推論：** 褐黃病主要病理為尿黑酸(homogentisic acid)代謝異常累積（如 alkaptonuria），與泛酸/CoA 代謝路徑無已知交集。目前無任何支持性試驗或文獻，純屬模型預測分數，無臨床或機轉基礎。

目前無相關臨床試驗登記，目前無相關文獻。

---

## 香港上市資訊

Pantothenic acid 目前在香港**未上市**，無登記許可證，無法提取核准適應症或劑型資訊。

---

## 安全性考量

安全性資訊請參考原廠仿單。（本評估包內主要警語、禁忌症與 DDI 資料均缺失，屬 Blocking 等級資料缺口，見下方結論。）

---

## 結論與下一步

**決策：Hold（整體）；「葉酸缺乏性貧血」候選可列為 Research Question**

**理由：**
- 5 個候選適應症中，4 個證據等級為 L4-L5，缺乏具特異性之泛酸介入證據，部分（先天性凝血酶原缺乏症、褐黃病）機轉上無合理連結或屬雜訊配對。
- 僅「葉酸缺乏性貧血」有較多筆試驗與文獻支持，且已進入 S1 決策階段，值得列為研究假設，但現有介入證據多來自多重營養素配方而非泛酸單獨介入，因果特異性仍弱。
- 藥物本身在香港未上市、無核准適應症、無 MOA 資料，且 TFDA/仿單警語與禁忌屬 Blocking 缺口（DG001），無法完成 S1 安全性初評。

**若要推進需要：**
- 補齊仿單警語/禁忌症資料（DG001，Blocking）
- 補齊作用機轉 (MOA) 資料（DG002，High）
- 針對「葉酸缺乏性貧血」設計泛酸單一成分之特異性介入研究，排除多重營養素混淆因子
- 確認香港（或其他司法管轄）之上市與許可證狀態
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

