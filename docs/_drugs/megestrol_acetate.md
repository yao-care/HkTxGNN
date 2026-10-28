---
layout: default
title: Megestrol Acetate
parent: 僅模型預測 (L5)
nav_order: 558
evidence_level: L5
indication_count: 7
monitor_inn: "MEGESTROL ACETATE"
predicted_indications: ["hereditary breast ovarian cancer syndrome", "borderline epithelial tumor of ovary", "uterine carcinosarcoma", "placenta cancer", "ovarian clear cell adenocarcinoma", "ovarian cancer", "malignant dysgerminomatous germ cell tumor of ovary"]
last_modified_at: 2026-10-23
description: "Megestrol Acetate：預測新適應症為遺傳性乳癌卵巢癌症候群（證據等級 L5）。原適應症：香港許可證資料未載明核准適應症"
---

# Megestrol Acetate
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

## 甲地孕酮 (Megestrol Acetate)：從子宮內膜癌到遺傳性乳癌卵巢癌症候群
{: .text-alpha }

## 一句話總結

甲地孕酮是一種黃體素類藥物。在知識圖譜中，它與子宮內膜癌有治療關聯記錄。
TxGNN 模型預測它可能對**遺傳性乳癌卵巢癌症候群 (Hereditary Breast Ovarian Cancer Syndrome)** 有效。
目前針對這個疾病**沒有任何臨床試驗或文獻**，預測僅來自模型分數。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 香港許可證資料未載明核准適應症；知識圖譜中記錄的關聯為子宮內膜癌（此為知識圖譜關聯，並非核准適應症） |
| 預測新適應症 | 遺傳性乳癌卵巢癌症候群 |
| TxGNN 預測分數 | 0.9989 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 6 張／共 6 張） |
| 許可證數 | 6 張（有效 6 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，甲地孕酮屬於黃體素類藥物。機轉上，黃體素訊號有可能影響 BRCA 相關乳房或卵巢組織的荷爾蒙反應，但這只是推測。

本次整理的資料沒有任何針對此症候群的臨床或文獻佐證。0.9989 的預測分數只代表模型內部的關聯強度，不能視為療效證據。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 其他預測候選（補充）

模型對同一藥物還預測了其他婦科腫瘤。以下僅作補充，不改變本報告對主要預測的結論。

| 預測疾病 | TxGNN 分數 | 證據等級 | 備註 |
|---------|-----------|---------|------|
| 卵巢交界性上皮腫瘤 | 0.9988 | L5 | 無試驗與文獻 |
| 子宮癌肉瘤 | 0.9984 | L5 | 僅有子宮肉瘤荷爾蒙受體研究（[19767065](https://pubmed.ncbi.nlm.nih.gov/19767065/)）與一篇個案報告（[31157684](https://pubmed.ncbi.nlm.nih.gov/31157684/)），皆非直接證明療效 |
| 胎盤癌 | 0.9984 | L5 | 無試驗與文獻 |
| 卵巢透明細胞腺癌 | 0.9980 | L5 | 無試驗與文獻；此組織型通常對荷爾蒙較不敏感 |
| 卵巢癌 | 0.9971 | L5（待查證） | 有高劑量甲地孕酮治療卵巢癌的 Phase 2 研究（[11593052](https://pubmed.ncbi.nlm.nih.gov/11593052/)、[9856656](https://pubmed.ncbi.nlm.nih.gov/9856656/)）。Phase 3 試驗 [NCT00005975](https://clinicaltrials.gov/study/NCT00005975) 針對乳癌治療後的熱潮紅，並非卵巢癌療效試驗，因此 L1 等級需重新評估 |
| 卵巢惡性無性細胞瘤 | 0.9966 | L5 | 無試驗與文獻；標準治療為手術與化療 |

## 香港上市資訊

香港許可證資料中，這 6 張的劑型與核准適應症欄位皆為空白，因此無法說明其核准用途。

| 許可證號 | 品名 | 製造商 |
|---------|------|--------|
| HK-60399 | MEGESIN TAB 160MG | TEVA PHARMACEUTICAL HONG KONG |
| HK-44293 | MEGAPLEX TAB 40MG | TEVA PHARMACEUTICAL HONG KONG |
| HK-68146 | MEGEJOHN TABLETS 40MG | SYNMOSA BIOPHARMA (HONG KONG) |
| HK-68644 | MEGESIA TABLETS 40MG | SB PHARMA LIMITED |
| HK-42289 | APO-MEGESTROL TAB 40MG | HIND WING CO LTD |

另有 HK-44543（MEGAPLEX TAB 160MG，TEVA PHARMACEUTICAL HONG KONG）。

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 荷爾蒙類（黃體素）藥物，並非傳統細胞毒性化療藥物 |
| 骨髓抑制風險 | 請參考原廠仿單的警語與注意事項 |
| 致吐性分級 | 請參考原廠仿單的警語與注意事項 |
| 監測項目 | 請參考原廠仿單的警語與注意事項 |
| 處置防護 | 請參考原廠仿單的警語與注意事項 |

## 安全性考量

- **知識圖譜中的禁忌關聯（非仿單內容）**：高血壓、腎臟疾病、肝臟疾病、膽囊疾病、高血糖、糖尿病及糖尿病酮酸中毒、腎上腺皮質功能不全（含 Addison 病）、男性性腺功能低下、提早停經、雄激素不敏感症候群等。
- **藥物交互作用**：共查得 100 筆，其中列出的 20 筆皆為中度。主要涉及：
  - 降血糖藥物，如 Metformin、Pioglitazone、Glimepiride、Repaglinide、Sitagliptin、Semaglutide、Dapagliflozin、Empagliflozin 及各類胰島素。
  - 其他藥物，如 Aprepitant 與 Clarithromycin。

  使用降血糖藥物的患者需留意血糖變化。

仿單層級的警語與禁忌請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 這個預測只有模型分數，沒有針對遺傳性乳癌卵巢癌症候群的臨床試驗或文獻，證據等級為 L5。
- 機轉資料也不足，且香港許可證資料未載明核准適應症。

**若要推進需要：**
- 補充甲地孕酮的作用機轉資料。
- 取得香港原廠仿單，確認核准適應症、警語與禁忌。
- 檢索 BRCA 突變相關族群使用黃體素類藥物的臨床與前臨床研究。
- 若要優先探索，卵巢癌（有 Phase 2 研究）與子宮癌肉瘤（有荷爾蒙受體研究）比本預測更值得先評估。卵巢癌需先查證 NCT00005975 的實際研究對象。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

