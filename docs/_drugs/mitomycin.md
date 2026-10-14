---
layout: default
title: Mitomycin
parent: 僅模型預測 (L5)
nav_order: 593
evidence_level: L5
indication_count: 5
---

# Mitomycin
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

# Mitomycin：從胰腺腺癌到胰臟骨質巨細胞瘤

## 一句話總結

Mitomycin（絲裂黴素）是一種細胞毒性抗腫瘤藥物，原本用於胰腺腺癌 (pancreatic adenocarcinoma) 的治療。
TxGNN 模型預測它可能對**胰臟破骨細胞型巨細胞瘤 (Osteoclastic giant cell tumor of pancreas)** 有效，
但目前**沒有臨床試驗和相關文獻**支持，僅屬於模型預測階段。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 胰腺腺癌 (pancreatic adenocarcinoma)（來自知識圖譜；香港許可證未載明適應症文字） |
| 預測新適應症 | 胰臟破骨細胞型巨細胞瘤 (Osteoclastic giant cell tumor of pancreas) |
| TxGNN 預測分數 | 99.86% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 4 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Mitomycin 屬於 DNA 烷化、交聯型的細胞毒性藥物，其在胰腺腺癌中的使用已被納入知識圖譜，機轉上可能適用於同屬胰臟外分泌腫瘤的相關亞型。

胰臟破骨細胞型巨細胞瘤是一種罕見的胰臟外分泌腫瘤變異型（具破骨細胞樣巨細胞的未分化癌），臨床上通常比照導管腺癌處理，因此以細胞毒性藥物治療在理論上說得通。

需要強調的是，這個預測分數只是計算模型的結果。本次彙整的資料中沒有任何臨床試驗或文獻直接評估 Mitomycin 對此疾病的效果。

同一批預測中還包括其他胰臟腫瘤，例如實性假乳突癌、混合分化型胰臟癌、胰管內乳突黏液癌及混合導管-內分泌癌，分數都在 99.84%–99.86% 之間。這些預測同樣只有模型分數支持，其中只有胰管內乳突黏液癌有一篇相關度不高的病例報告。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

（附註：排名第 4 的預測「胰管內乳突黏液癌」檢索到一篇 2005 年病例報告（PMID [15983445](https://pubmed.ncbi.nlm.nih.gov/15983445/)），內容為偽黏液瘤腹膜炎合併胰臟 IPMN，並未評估 Mitomycin 的療效，不視為支持證據。）

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-67642 | ACCORD MITOMYCIN 2 POWDER FOR SOLUTION FOR INJECTION/INFUSION OR INTRAVESICAL USE 2MG | 注射用粉末 | 未提供 |
| HK-67641 | ACCORD MITOMYCIN 10 POWDER FOR SOLUTION FOR INJECTION/INFUSION OR INTRAVESICAL USE 10MG | 注射用粉末 | 未提供 |
| HK-66821 | MITONCO POWDER FOR SOLUTION FOR INJECTION 10MG | 注射用粉末 | 未提供 |
| HK-67651 | MITOMYCIN FOR INJECTION USP 10MG | 注射用粉末 | 未提供 |

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 傳統細胞毒性藥物（DNA 烷化／交聯型抗腫瘤抗生素） |
| 骨髓抑制風險 | 高（知識圖譜顯示血小板減少、白血球減少、貧血為禁忌相關疾病） |
| 致吐性分級 | 請參考原廠仿單 |
| 監測項目 | CBC（含血小板、白血球分類）、腎功能、心臟功能 |
| 處置防護 | 需依細胞毒性藥物處置規範操作 |

## 安全性考量

- **知識圖譜顯示的禁忌相關疾病**（非仿單文字）：腎臟疾病、輸尿管積膿、血小板減少、凝血疾病、貧血（含巨球性貧血）、白血球減少、溶血性尿毒症候群（含典型）、充血性心衰竭、心臟衰竭、口腔炎。
- **藥物交互作用**：共查得 100 筆，以下為較重要者：
  - 重大 (Major)：Deferiprone、Samarium (153Sm) lexidronam
  - 中度 (Moderate)：Palifermin、Strontium chloride Sr-89、Fostamatinib
  - 輕微 (Minor)：Levofloxacin
  - 其餘（如 Warfarin、Leucovorin、Dexamethasone 等）等級未定

  上述藥物多與骨髓抑制疊加有關，合併使用時須謹慎。

仿單警語與禁忌的詳細內容請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 預測分數雖高（99.86%），但沒有臨床試驗與文獻支持，證據等級僅為 L5。
- 這是罕見腫瘤，Mitomycin 的作用機轉資料也有缺口，且其骨髓抑制風險高，目前不宜推進。

**若要推進需要：**
- 補齊 Mitomycin 的作用機轉（MOA）資料
- 取得香港仿單的警語、禁忌與核准適應症文字
- 搜尋 Mitomycin 用於胰臟罕見腫瘤亞型的病例報告、回顧性研究或臨床試驗
- 與病理及腫瘤專科確認此亞型是否適合以現有胰腺腺癌方案處理
- 若進入評估，須制定血液學與腎功能監測計畫
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

