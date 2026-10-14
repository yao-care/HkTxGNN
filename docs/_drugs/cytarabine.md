---
layout: default
title: Cytarabine
parent: 中證據等級 (L3-L4)
nav_order: 240
evidence_level: L4
indication_count: 9
---

# Cytarabine
{: .fs-9 }

證據等級: **L4** | 預測適應症: **9** 個
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

# Cytarabine：從急性白血病到小細胞肺癌

## 一句話總結

Cytarabine（阿糖胞苷）是嘧啶核苷類抗代謝藥物，原本用於急性淋巴芽細胞白血病與急性骨髓性白血病等血液惡性腫瘤。
TxGNN 模型預測它可能對**小細胞肺癌 (Small Cell Lung Carcinoma)** 有效，但目前**沒有相關臨床試驗登記**，且現有文獻多針對非小細胞肺癌或體外研究，證據相當有限。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 急性淋巴芽細胞白血病、急性骨髓性白血病（來自知識圖譜；香港許可證未提供適應症文字） |
| 預測新適應症 | 小細胞肺癌 (Small Cell Lung Carcinoma) |
| TxGNN 預測分數 | 99.78% |
| 證據等級 | L4 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 14 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（MOA）。根據已知資訊，Cytarabine 是嘧啶核苷類抗代謝藥物，可抑制快速分裂細胞的 DNA 合成。這在機轉上是合理的依據，因為小細胞肺癌是增殖快速的腫瘤。

不過，原適應症（白血病）與小細胞肺癌在腫瘤類型上差異很大。現有文獻主要來自非小細胞肺癌（NSCLC）的高劑量 cytarabine 合併 cisplatin 的 Phase II 試驗，其反應率僅約 14%，且血液毒性明顯。另有一篇 1987 年的小細胞肺癌高劑量 cytarabine 報告，但缺乏摘要可供評估。此外，文獻也指出多數實體腫瘤對 cytarabine 不敏感。因此，兩者之間的連結屬於間接推論。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [2156598](https://pubmed.ncbi.nlm.nih.gov/2156598/) | 1990 | Phase II | Cancer | 高劑量 cytarabine 合併 cisplatin 用於未治療的 NSCLC（37 人），整體反應率 14%，32% 發生 IV 級骨髓抑制，4 人於試驗期間死亡 |
| [2157307](https://pubmed.ncbi.nlm.nih.gov/2157307/) | 1990 | Phase II | Tumori | Cytarabine + cisplatin + vindesine 用於晚期 NSCLC（32 人） |
| [2158614](https://pubmed.ncbi.nlm.nih.gov/2158614/) | 1990 | 隨機 Phase II | Med Pediatr Oncol | CALGB 比較 cisplatin-cytarabine 與 cisplatin-vinblastine 用於晚期 NSCLC（151 人） |
| [3030547](https://pubmed.ncbi.nlm.nih.gov/3030547/) | 1987 | 臨床報告 | Cancer Treat Rep | 高劑量 cytarabine 用於小細胞肺癌（無摘要） |
| [1332622](https://pubmed.ncbi.nlm.nih.gov/1332622/) | 1992 | Review | Gan To Kagaku Ryoho | 說明 cytarabine 對白血病有效，但多數實體腫瘤不敏感；介紹結構相關的 gemcitabine 與 DMDC |
| [9561978](https://pubmed.ncbi.nlm.nih.gov/9561978/) | 1998 | 臨床報告 | Arch Neurol | NSCLC 癌性腦膜炎的綜合治療 |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-65688 | ACCORD CYTARABINE SOLUTION FOR INJECTION/INFUSION 100MG/1ML | 注射劑 | 未提供 |
| HK-36387 | CYTARABINE INJ 100MG/ML | 注射劑 | 未提供 |
| HK-66210 | CYTARABINE KABI SOLUTION FOR INJECTION OR INFUSION 100MG/1ML | 注射劑 | 未提供 |
| HK-27972 | CYTOSAR STERILE POWDER FOR INJ 100MG | 注射用粉劑 | 未提供 |
| HK-44691 | ALEXAN INJ 5% | 注射劑 | 未提供 |

---

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 傳統細胞毒性藥物（嘧啶核苷類抗代謝藥物） |
| 骨髓抑制風險 | 高（相關文獻顯示高劑量合併 cisplatin 時，32% 患者出現 IV 級骨髓抑制） |
| 致吐性分級 | 請參考原廠仿單 |
| 監測項目 | 血液學參數（CBC 含分類）、肝腎功能 |
| 處置防護 | 需依細胞毒性藥物處置規範操作 |

---

## 安全性考量

- **知識圖譜中標示的相關疾病風險**（此為模型資料，非仿單文字）：腎臟疾病、肝臟疾病、胰臟炎、血小板低下、白血球低下、嗜中性白血球低下、顆粒球缺乏症、貧血、周邊神經病變、腹瀉性疾病、肺水腫、壞死性腸炎等。
- **藥物交互作用**：資料庫共查得 100 筆。其中列為中度的有 Naltrexone；輕度的有 Levofloxacin；其餘多數等級未明。

香港仿單的警語與禁忌症資料尚未取得，請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 預測分數雖高，但沒有任何針對小細胞肺癌的臨床試驗，現有文獻多為 NSCLC 的老舊 Phase II 研究（反應率低、血液毒性高）及體外研究。
- 作用機轉資料與仿單安全性資料皆缺漏，無法進入安全性篩選。

**若要推進需要：**
- 補齊 DrugBank 的作用機轉（MOA）資料
- 取得香港衛生署的仿單，確認警語、禁忌症及核准適應症
- 針對小細胞肺癌的直接證據（如細胞株、動物模型或早期臨床試驗）
- 與現行小細胞肺癌標準療法（如鉑類加 etoposide）比較其潛在價值

---

### 附註：其他預測適應症

| 預測適應症 | TxGNN 分數 | 證據等級 | 說明 |
|-----------|-----------|---------|------|
| 原發性肺淋巴瘤 | 99.78% | L4 | 文獻多為其他淋巴瘤（如 CNS 淋巴瘤），屬間接證據 |
| 上消化道腫瘤 | 99.49% | L4 | 有一項高劑量 cytarabine 增強 cisplatin 用於頭頸癌的研究，其餘多為間接資料 |
| 後腹膜腫瘤 | 99.23% | L4 | 多為髓樣肉瘤與淋巴瘤病例報告 |
| 神經母細胞瘤 | 99.19% | L4 | 僅有體外研究，3 個相關試驗均未測試 cytarabine，列為研究問題 |
| 高分化胎兒型肺腺癌、肺母細胞瘤、神經節母細胞瘤、椎體異常合併內分泌與 T 細胞功能異常 | 99.32%–99.76% | L5 | 僅有模型預測，無試驗或文獻 |
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

