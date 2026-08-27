---
layout: default
title: Ibritumomab Tiuxetan
parent: 僅模型預測 (L5)
nav_order: 382
evidence_level: L5
indication_count: 5
---

# Ibritumomab Tiuxetan
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

# Ibritumomab Tiuxetan：從 CD20+ B 細胞淋巴瘤到急性淋巴性白血病

## 一句話總結

Ibritumomab Tiuxetan（DrugBank ID: DB00078）為抗 CD20 單株抗體之放射免疫共軛物，原用於治療 CD20 陽性 B 細胞非何杰金氏淋巴瘤（NHL，此為外部藥理知識補充，非官方登記資料）。
TxGNN 模型預測它可能對**急性淋巴性/淋巴母細胞白血病（Acute Lymphoblastic/Lymphocytic Leukemia）**有效，
但目前**無任何臨床試驗或文獻**支持，且機轉合理性存在疑慮。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | CD20+ B 細胞非何杰金氏淋巴瘤（NHL）※外部藥理知識推論，非香港/台灣官方登記資料 |
| 預測新適應症 | 急性淋巴性/淋巴母細胞白血病 (Acute Lymphoblastic/Lymphocytic Leukemia) |
| TxGNN 預測分數 | 99.78% |
| 證據等級 | L5 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（DrugBank MOA 欄位為資料缺口）。根據已知的藥理分類，Ibritumomab Tiuxetan 是一種抗 CD20 單株抗體與釔-90（Y-90）放射性核種結合的放射免疫治療藥物，其標靶為成熟 B 細胞表面的 CD20 抗原。

然而，急性淋巴性白血病（ALL）多數細胞來源為前驅 B 細胞（pre-B）或 T 系淋巴母細胞，CD20 表現率僅約 30-50%，且多見於成熟 B-ALL/Burkitt 型白血病等特定亞型，表現強度通常也低於淋巴瘤細胞的高密度 CD20 表現。換言之，此藥物的核心作用標的與 ALL 多數病例的抗原特徵並不完全吻合。

TxGNN 分數高達 99.78%，但這類知識圖譜嵌入分數容易受「淋巴系統惡性腫瘤」語意群聚效應影響，未必反映實際抗原表現量與放射免疫治療的臨床適用性。值得注意的是，同一評估中排名第 2-5 的候選適應症（Burkitt 淋巴瘤、MALT 淋巴瘤等）皆屬於典型 CD20 高陽性成熟 B 細胞淋巴瘤，與 Ibritumomab Tiuxetan 原核准適應症的藥理機轉一致性更高，這也是系統將本項（急性淋巴性白血病）的建議標記為「Hold」，而其餘候選標記為「Research Question」的原因。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 香港上市資訊

Ibritumomab Tiuxetan 目前在香港**未上市**，無任何藥品許可證登記（0 張）。

---

## 細胞毒性

Ibritumomab Tiuxetan 屬於抗腫瘤藥物（放射免疫治療用於血液系統惡性腫瘤）。

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 標靶放射免疫治療（抗 CD20 單株抗體 + Y-90 放射性核種共軛物，非傳統細胞毒性化療藥物） |
| 骨髓抑制風險 | 請參考原廠仿單的警語與注意事項 |
| 致吐性分級 | 請參考原廠仿單的警語與注意事項 |
| 監測項目 | 請參考原廠仿單的警語與注意事項 |
| 處置防護 | 請參考原廠仿單的警語與注意事項 |

---

## 安全性考量

安全性資訊請參考原廠仿單。

（註：本評估的 TFDA/香港仿單警語與禁忌資料為 Blocking 等級資料缺口，尚無法進行 S1 安全性初評。）

---

## 結論與下一步

**決策：Hold**

**理由：**
- 急性淋巴性白血病多數亞型 CD20 表現率低且不穩定，與藥物核心作用機轉的匹配度存疑；
- 完全無臨床試驗或文獻證據支持（證據等級 L5，僅有模型預測分數）；
- 作用機轉資料與仿單安全性資料均為缺口，無法進行基礎安全性評估。

**若要推進需要：**
- 補齊 Ibritumomab Tiuxetan 的正式作用機轉（MOA）資料
- 取得 TFDA/香港仿單警語與禁忌症資料，解除 Blocking 等級資料缺口
- 確認 ALL 目標族群（如成熟 B-ALL/Burkitt 型白血病亞型）的 CD20 表現率與強度
- 建議優先評估同批預測中機轉一致性更高的候選適應症（如 Burkitt 淋巴瘤、MALT 淋巴瘤等，標記為 Research Question），而非直接推進本項急性淋巴性白血病適應症
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

