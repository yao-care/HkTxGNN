---
layout: default
title: Gimeracil
parent: 高證據等級 (L1-L2)
nav_order: 414
evidence_level: L1
indication_count: 7
monitor_inn: "GIMERACIL"
predicted_indications: ["colonic neoplasm", "cecum villous adenoma", "lipoma of colon", "cecum neuroendocrine tumor G1", "rectosigmoid junction neoplasm", "colonic lymphangioma", "colon leiomyoma"]
last_modified_at: 2026-10-23
description: "Gimeracil：預測新適應症為大腸腫瘤（證據等級 L1）。原適應症：胃癌"
---

# Gimeracil
{: .fs-9 }

證據等級: **L1** | 預測適應症: **7** 個
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

## Gimeracil：從胃癌到大腸腫瘤
{: .text-alpha }

## 一句話總結

Gimeracil 是 S-1 複方（tegafur／gimeracil／oteracil）的成分之一，在知識圖譜中記錄的相關疾病為胃癌。
TxGNN 模型預測它可能對**大腸腫瘤 (Colonic Neoplasm)** 有效。
目前有 **6 個臨床試驗**和 **12 篇文獻**與此方向相關，但臨床試驗皆為 S-1 複方的研究，並非 gimeracil 單獨使用。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 胃癌（知識圖譜記錄的關聯；香港許可證資料未載明核准適應症文字） |
| 預測新適應症 | 大腸腫瘤 |
| TxGNN 預測分數 | 0.9988 |
| 證據等級 | L1 |
| 香港上市 | 上市中（有效許可證 4 張／共 4 張） |
| 許可證數 | 4 張（有效 4 張） |
| 建議決策 | Proceed with Guardrails |

## 為什麼這個預測合理？

目前缺乏經資料庫確認的詳細作用機轉資料。根據已知資訊，Gimeracil 是二氫嘧啶脫氫酶（DPD）抑制劑，也是 S-1 複方的一部分。它抑制 5-FU 的分解，使 tegafur 所產生的 5-FU 維持較高且持久的血中濃度。

5-FU 的細胞毒性機轉（抑制胸苷酸合成酶，以及代謝物嵌入 RNA／DNA）對胃癌與大腸直腸癌同樣適用，因為兩者都屬於對 5-FU 敏感的消化道腫瘤。Gimeracil 本身不是細胞毒性成分，而是藥物動力學的增強劑。

需注意：支持證據來自 S-1 複方，而非 gimeracil 單獨使用。TxGNN 的高分與臨床資料方向一致，但不能直接視為 gimeracil 單一成分的療效證明。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00660894](https://clinicaltrials.gov/study/NCT00660894) | Phase 3 | 完成 | 1535 | UFT＋leucovorin 對比 TS-1（S-1），用於 Stage III 結腸癌術後輔助治療 |
| [NCT03448549](https://clinicaltrials.gov/study/NCT03448549) | Phase 3 | 未知 | 1191 | SOX 對比 XELOX，用於 Stage III 大腸直腸癌輔助化療 |
| [NCT00974389](https://clinicaltrials.gov/study/NCT00974389) | Phase 2 | 未知 | 40 | S-1＋bevacizumab，用於前線化療失敗後的不可切除或復發大腸直腸癌 |
| [NCT02618356](https://clinicaltrials.gov/study/NCT02618356) | Phase 2 | 未知 | 82 | Raltitrexed＋S-1，用於標準化療失敗的轉移性大腸直腸癌，主要終點為無惡化存活期 |
| [NCT06255379](https://clinicaltrials.gov/study/NCT06255379) | Phase 2 | 尚未招募 | 52 | Fruquintinib＋tegafur/gimeracil/oteracil，用於晚期轉移性大腸直腸癌三線治療（單臂） |
| [NCT02216149](https://clinicaltrials.gov/study/NCT02216149) | Phase 2 | 已終止 | 20 | S-1 或 capecitabine＋oxaliplatin 對冠狀動脈血流的影響（心臟安全性終點，非療效） |

## 文獻證據

目前未檢索到 RCT 等級的文獻，以下為較相關者，以研究類型排序：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [21084813](https://pubmed.ncbi.nlm.nih.gov/21084813/) | 2010 | 回溯性分析 | Gan To Kagaku Ryoho | 87 位晚期或復發結腸癌患者接受 S-1＋irinotecan，第 3–4 級血液毒性發生率為 16.1%，並分析其風險因子 |
| [20841935](https://pubmed.ncbi.nlm.nih.gov/20841935/) | 2010 | 藥物動力學研究 | Gan To Kagaku Ryoho | 以小鼠腹膜轉移模型評估 S-1 用於結腸癌腹膜轉移的可行性 |
| [20811661](https://pubmed.ncbi.nlm.nih.gov/20811661/) | 2010 | 前臨床（異種移植） | Oncology Reports | Irinotecan 可降低腫瘤內胸苷酸合成酶，克服結腸癌異種移植對 5-FU 的抗藥性，並增強與口服 S-1 的抗腫瘤效果 |
| [32936722](https://pubmed.ncbi.nlm.nih.gov/32936722/) | 2021 | 病例報告與文獻回顧 | J Oncol Pharm Pract | S-1 引起高三酸甘油酯血症 |
| [28414195](https://pubmed.ncbi.nlm.nih.gov/28414195/) | 2017 | 病例報告 | Eur J Dermatol | TS-1 引起紅皮症、廣泛黏膜受損及手足症候群 |
| [18630468](https://pubmed.ncbi.nlm.nih.gov/18630468/) | 2008 | 病例報告 | Anticancer Res | S-1＋CPT-11 用於結腸癌肝轉移，達到並維持完全緩解 |
| [29394831](https://pubmed.ncbi.nlm.nih.gov/29394831/) | 2017 | 病例報告 | Gan To Kagaku Ryoho | SOX＋panitumumab 降階化療後，對不可切除大腸直腸癌肝轉移施行兩階段肝切除 |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-67976 | TEGO CAPSULES 20MG/5.8MG/19.6MG | 未載明 | 未載明 |
| HK-67977 | TEGO CAPSULES 25MG/7.25MG/24.5MG | 未載明 | 未載明 |
| HK-61181 | TS-ONE 25 CAP | 未載明 | 未載明 |
| HK-61182 | TS-ONE 20 CAP | 未載明 | 未載明 |

## 細胞毒性

Gimeracil 本身不是細胞毒性成分，但它屬於 S-1（氟嘧啶類）複方，會增強 5-FU 的暴露量，因此以複方使用時需視為細胞毒性化療。

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 傳統細胞毒性藥物複方的一部分（氟嘧啶類，gimeracil 為 DPD 抑制劑） |
| 骨髓抑制風險 | 中度。S-1＋irinotecan 研究中第 3–4 級血液毒性約 16.1% |
| 致吐性分級 | 請參考原廠仿單 |
| 監測項目 | 血球計數（CBC，含分類）、肝腎功能 |
| 處置防護 | 請參考原廠仿單的警語與注意事項 |

## 安全性考量

安全性資訊請參考原廠仿單。

文獻中另有 S-1 相關不良反應的病例報告，包括高三酸甘油酯血症、紅皮症與手足症候群，可作為監測參考。

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 有 2 個大型 Phase 3 試驗（其中 NCT00660894 已完成，n=1535）直接研究含 gimeracil 的 S-1 於大腸或結腸癌，並有多個 Phase 2 試驗支持。
- 但證據皆針對 S-1 複方，並非 gimeracil 單獨使用，且多數試驗狀態為「未知」，安全性資料也不完整。

**若要推進需要：**
- 取得 NCT00660894 與 NCT03448549 的已發表結果，確認療效與安全性結論
- 取得香港許可證的核准適應症文字與原廠仿單（警語、禁忌症），確認 S-1 製劑現行核准範圍
- 補充 gimeracil 的作用機轉資料（DrugBank）
- 明確界定本評估對象為 S-1 複方，而非 gimeracil 單一成分
- 制定血液毒性、手足症候群等不良反應的監測計畫

**其他預測適應症（排名 2–7）：** 盲腸絨毛狀腺瘤、結腸脂肪瘤、盲腸神經內分泌腫瘤 G1、結腸淋巴管瘤、結腸平滑肌瘤皆無相關證據，證據等級為 L5，建議 Hold。直腸乙狀結腸交界處腫瘤僅能由大腸直腸癌試驗間接推論，並無針對該疾病的研究，證據等級同樣視為 L5，宜併入大腸直腸癌適應症一併評估。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

