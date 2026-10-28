---
layout: default
title: Sunitinib
parent: 高證據等級 (L1-L2)
nav_order: 844
evidence_level: L2
indication_count: 5
monitor_inn: "SUNITINIB"
predicted_indications: ["liposarcoma", "ovarian myxoid liposarcoma", "dermatofibrosarcoma protuberans", "angiolipoma", "heart fibrosarcoma"]
last_modified_at: 2026-10-23
description: "Sunitinib：預測新適應症為脂肪肉瘤 (Liposarcoma)（證據等級 L2）。原適應症：知識圖譜中記錄的關聯為腎細胞癌、透明細胞腎癌、胃腸道基質瘤"
---

# Sunitinib
{: .fs-9 }

證據等級: **L2** | 預測適應症: **5** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## 藥師評估報告

</div>

## Sunitinib：從腎細胞癌到脂肪肉瘤
{: .text-alpha }

## 一句話總結

Sunitinib 是一種口服多標靶酪胺酸激酶抑制劑，知識圖譜中記錄的使用方向為腎細胞癌與胃腸道基質瘤。
TxGNN 模型預測它可能對**脂肪肉瘤 (Liposarcoma)** 有效。
目前有 **2 個軟組織肉瘤相關的 Phase 2 臨床試驗**，以及 **1 篇直接納入脂肪肉瘤的 Phase 2 研究**和 1 篇個案報告。但這些研究的脂肪肉瘤亞組結果有限。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 知識圖譜中記錄的關聯為腎細胞癌、透明細胞腎癌、胃腸道基質瘤（香港許可證資料未載明核准適應症文字） |
| 預測新適應症 | 脂肪肉瘤 (Liposarcoma) |
| TxGNN 預測分數 | 0.9987 |
| 證據等級 | L2 |
| 香港上市 | 上市中（有效許可證 6 張／共 6 張） |
| 許可證數 | 6 張（有效 6 張） |
| 建議決策 | Proceed with Guardrails |

## 為什麼這個預測合理？

Sunitinib 是多標靶受體酪胺酸激酶抑制劑，作用標的包括 VEGFR、PDGFR、KIT、FLT3 和 RET。目前缺乏 DrugBank 詳細的作用機轉資料，以上機轉是根據對該藥物的一般認識推論。

抗血管新生與抑制 PDGFR 的活性，為軟組織肉瘤提供了合理的生物學基礎。不過脂肪肉瘤主要由 MDM2/CDK4 擴增驅動，與 sunitinib 的標靶並不直接相關，因此機轉上的連結屬於間接。

TxGNN 分數很高，但那是計算預測。實際支持來自對軟組織肉瘤的 Phase 2 研究，其中一項專門針對平滑肌肉瘤、脂肪肉瘤與惡性纖維組織細胞瘤三種亞型。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00474994](https://clinicaltrials.gov/study/NCT00474994) | Phase 2 | 完成 | 53 | 連續劑量 sunitinib 用於非 GIST 肉瘤；為單臂設計，脂肪肉瘤亞組結果未見於現有資料 |
| [NCT00400569](https://clinicaltrials.gov/study/NCT00400569) | Phase 2 | 完成 | 48 | sunitinib 用於轉移性或無法手術切除的軟組織肉瘤（納入脂肪肉瘤等亞型）；開放標籤，脂肪肉瘤的實際結果無法由現有資料判斷 |

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [21154746](https://pubmed.ncbi.nlm.nih.gov/21154746/) | 2011 | Phase 2 試驗 | Int J Cancer | sunitinib 用於復發或難治性軟組織肉瘤，聚焦平滑肌肉瘤、脂肪肉瘤與惡性纖維組織細胞瘤三種亞型 |
| [23482782](https://pubmed.ncbi.nlm.nih.gov/23482782/) | 2013 | 個案報告 | Anticancer Res | 一例重度前線治療後的轉移性脂肪肉瘤，sunitinib 帶來長期臨床獲益 |
| [24555529](https://pubmed.ncbi.nlm.nih.gov/24555529/) | 2014 | Review | Expert Rev Anticancer Ther | 成人軟組織肉瘤的新興療法 |
| [24712007](https://pubmed.ncbi.nlm.nih.gov/24712007/) | 2014 | Review | Magyar Onkologia | 依組織學亞型選擇軟組織肉瘤的藥物治療 |
| [22987955](https://pubmed.ncbi.nlm.nih.gov/22987955/) | 2012 | Review | Ann Oncol | 組織學導向與非組織學導向的軟組織肉瘤治療；trabectedin 對脂肪肉瘤有活性 |
| [38254762](https://pubmed.ncbi.nlm.nih.gov/38254762/) | 2024 | Review／分子分析 | Cancers | 脂肪肉瘤的基因、表觀遺傳與轉錄體變異，用於標靶治療選擇 |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-55406 | SUTENT CAP 12.5MG | 膠囊（品項名稱所示） | 現有資料未載明 |
| HK-55405 | SUTENT CAP 50MG | 膠囊（品項名稱所示） | 現有資料未載明 |
| HK-67681 | ALSUNI CAPSULES 12.5MG | 膠囊 | 現有資料未載明 |
| HK-67682 | ALSUNI CAPSULES 50MG | 膠囊 | 現有資料未載明 |
| HK-68626 | SUNITINIB CAPSULES 12.5MG | 膠囊 | 現有資料未載明 |

另有 1 張許可證（HK-68627，SUNITINIB CAPSULES 50MG）未列於上表，共 6 張，皆為單方且有效。

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 標靶藥物（多標靶酪胺酸激酶抑制劑） |
| 骨髓抑制風險 | 請參考原廠仿單；知識圖譜記錄血小板低下與貧血為禁忌相關疾病 |
| 致吐性分級 | 請參考原廠仿單 |
| 監測項目 | 建議監測 CBC、肝功能、甲狀腺功能、心功能與 QT 間期、電解質 |
| 處置防護 | 請參考原廠仿單與院內抗腫瘤藥物處置規範 |

## 安全性考量

- **知識圖譜記錄的禁忌相關疾病**（非仿單文字）：長 QT 症候群、尖端扭轉型心室頻脈、肝衰竭與肝病、藥物性肝損傷、心臟衰竭、血小板低下、貧血、甲狀腺功能低下與亢進、腎上腺功能不全、胰臟炎、癲癇、後部可逆性腦病變症候群、高膽紅素血症（含 Gilbert 症候群）、膽囊疾病、缺鉀。
- **藥物交互作用**：共查到 100 筆，下列為部分。
  - 重大（Major）：Dolasetron。
  - 中度（Moderate）：Clarithromycin、Dexamethasone、Famotidine、Loperamide、Palonosetron、Glimepiride、Chlorpropamide 及多種胰島素。
  - 這些與 QT 延長、CYP3A4 代謝及血糖變化的風險有關，臨床使用時需審視並用藥物。

仿單的警語與禁忌請參考原廠仿單。

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 有 1 篇直接納入脂肪肉瘤的 Phase 2 研究，以及 2 個已完成的軟組織肉瘤 Phase 2 試驗，證據等級為 L2。
- 但脂肪肉瘤亞組的療效資料有限，且機轉連結間接，因此只適合在嚴格控管下，以研究性或個別化方式推進。

**若要推進需要：**
- 取得上述試驗中脂肪肉瘤亞組的客觀緩解率與無惡化存活期等結果。
- 與目前脂肪肉瘤已建立的治療（如 trabectedin）比較。
- 取得香港許可證的核准適應症文字與仿單警語、禁忌。
- 制定心臟、肝臟、甲狀腺與血液學的安全性監測計畫，以及 QT 相關藥物交互作用的檢核流程。
- 補充 DrugBank 的作用機轉資料。

---

**其他預測適應症的簡要狀況**（參考）：
- 皮膚纖維肉瘤 (Dermatofibrosarcoma protuberans)：L3，有 imatinib 抗藥後使用的回顧性系列與個案報告，機轉（PDGFRB 活化）合理。
- 卵巢黏液性脂肪肉瘤、血管脂肪瘤、心臟纖維肉瘤：缺乏直接證據，建議暫緩。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

