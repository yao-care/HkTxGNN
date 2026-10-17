---
layout: default
title: Tipiracil
parent: 僅模型預測 (L5)
nav_order: 882
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Tipiracil：預測新適應症為盲腸絨毛狀腺瘤 (Cecum Villous Adenoma)（證據等級 L5）。原適應症：大腸直腸癌（惡性結腸腫瘤）"
monitor_inn: "TIPIRACIL"
predicted_indications: ["cecum villous adenoma", "lipoma of colon", "rectosigmoid junction neoplasm", "cecum neuroendocrine tumor G1", "colonic lymphangioma"]
---

# Tipiracil
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Tipiracil：從大腸直腸癌到盲腸絨毛狀腺瘤

## 一句話總結

Tipiracil 是 trifluridine/tipiracil（Lonsurf）複方的成分之一，原本用於轉移性大腸直腸癌治療。
TxGNN 模型預測它可能對**盲腸絨毛狀腺瘤 (Cecum Villous Adenoma)** 有效，
但目前**沒有任何臨床試驗或文獻**支持，僅屬模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 大腸直腸癌（惡性結腸腫瘤）；香港許可證未提供核准適應症文字，此為知識圖譜的適應症資料 |
| 預測新適應症 | 盲腸絨毛狀腺瘤 (Cecum Villous Adenoma) |
| TxGNN 預測分數 | 99.99% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 2 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Tipiracil 是 trifluridine/tipiracil 複方的一部分，該複方在大腸直腸癌中的療效已被證實。Tipiracil 本身是胸苷磷酸化酶（thymidine phosphorylase）抑制劑，作用是保護 trifluridine 不被降解，本身沒有已知的直接抗腫瘤活性。

盲腸絨毛狀腺瘤是大腸的癌前病變，與已核准的大腸直腸癌在解剖位置和生物學上有鬆散關聯。這很可能是 TxGNN 高分的主因：知識圖譜中它與大腸直腸癌相鄰。

不過，目前沒有任何臨床或文獻證據支持用於良性或癌前腺瘤。細胞毒性複方用於癌前病變，風險效益比也需要審慎評估。這個高分應視為計算預測，不應視為療效訊號。

其他排名靠前的預測（結腸脂肪瘤、直腸乙狀結腸交界腫瘤、盲腸神經內分泌腫瘤 G1、結腸淋巴管瘤）同樣沒有證據。其中直腸乙狀結腸交界腫瘤很可能已涵蓋在現有大腸直腸癌適應症內，屬於標示範圍的問題，並非真正的藥物再利用。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-65361 | LONSURF TABLETS 20MG/8.19MG | 未提供 | 未提供 |
| HK-65360 | LONSURF TABLETS 15MG/6.14MG | 未提供 | 未提供 |

兩張許可證均為單方登記，持證商為 DKSH Hong Kong Limited，狀態皆為有效。

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 與 trifluridine（核苷類抗代謝藥物）組成複方；Tipiracil 本身為酶抑制劑，用於保護 trifluridine |
| 骨髓抑制風險 | 請參考原廠仿單的警語與注意事項 |
| 致吐性分級 | 請參考原廠仿單的警語與注意事項 |
| 監測項目 | 請參考原廠仿單的警語與注意事項（一般包含血液學與肝腎功能監測） |
| 處置防護 | 請參考原廠仿單的警語與注意事項 |

## 安全性考量

- **藥物交互作用**：已查詢到 14 筆紀錄，其中 13 筆為中度交互作用（DDInter），包括：
  - Cimetidine
  - Tafenoquine
  - Ketoconazole
  - Brigatinib
  - Crizotinib
  - Encorafenib
  - Ethinylestradiol
  - Lenvatinib
  - Medroxyprogesterone acetate
  - Megestrol acetate
  - Ribociclib
  - Rucaparib
  - Vandetanib
- 另有 1 筆藥理學資料顯示 Tipiracil 與 SARS-CoV-2 的 CoV 非結構蛋白 15 有靶點關聯，未標示嚴重度，僅屬藥理學資料，臨床意義不明。

警語與禁忌症資料尚未取得，請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 所有預測適應症都只有模型分數，沒有臨床試驗或文獻佐證（證據等級 L5）。
- 盲腸絨毛狀腺瘤屬癌前或良性病變，使用細胞毒性複方的風險效益比不明，且 Tipiracil 本身沒有直接抗腫瘤作用。

**若要推進需要：**
- 取得 Tipiracil 的作用機轉資料，以分析機轉上的關聯
- 取得香港仿單的警語與禁忌症，完成安全性篩選
- 補齊香港許可證的核准適應症與劑型資料，並確認直腸乙狀結腸交界腫瘤是否已在現有標示範圍內
- 進行系統性文獻與臨床試驗檢索，確認是否有腺瘤或癌前病變的相關研究
- 評估是否有其他較合理的預測適應症可作優先驗證
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

