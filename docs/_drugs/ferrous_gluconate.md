---
layout: default
title: Ferrous Gluconate
parent: 中證據等級 (L3-L4)
nav_order: 316
evidence_level: L4
indication_count: 5
---

# Ferrous Gluconate
{: .fs-9 }

證據等級: **L4** | 預測適應症: **5** 個
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

以下是根據 Evidence Pack 產生的評估報告：

---

# 葡萄糖酸亞鐵：從缺鐵性貧血到 Plummer-Vinson 症候群

## 一句話總結

葡萄糖酸亞鐵（Ferrous Gluconate）是常用的二價鐵口服補充劑，臨床上用於補充鐵質、改善缺鐵性貧血。
TxGNN 模型預測它可能對 **Plummer-Vinson 症候群（Patterson-Kelly 症候群）** 有效，
目前 **無直接臨床試驗或文獻**，但機轉連結極強——此症候群的核心病理即為慢性缺鐵，屬間接證據缺口而非機轉缺口。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 缺鐵性貧血（補鐵劑） |
| 預測新適應症 | Plummer-Vinson 症候群 |
| TxGNN 預測分數 | 99.94% |
| 證據等級 | L4 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

Ferrous gluconate 是一種二價鐵（Fe²⁺）鹽類補充劑，在腸道吸收後可直接補充體內鐵庫存，用於治療缺鐵性貧血。目前缺乏詳細的作用機轉資料，但作為鐵補充劑的藥理作用已被充分確立。

Plummer-Vinson 症候群（PVS）的核心病理機轉即為**長期慢性缺鐵**：缺鐵導致食道及咽部黏膜組織萎縮，進而形成食道蹼（esophageal web），造成吞嚥困難。因此，補充鐵質可直接逆轉造成疾病的缺鐵狀態，機轉關聯性在已知病症中屬最高層級——病因即為藥物的治療靶點。

雖然本次 Evidence Pack 中無針對 Plummer-Vinson 症候群的臨床試驗或文獻登錄，但此屬**間接證據缺口**（資料庫收錄不全），而非機轉缺口。鐵劑治療 PVS 在臨床實踐中屬已建立的知識，TxGNN 模型的高預測分數（99.94%）符合此臨床共識。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 香港上市資訊

葡萄糖酸亞鐵目前在香港尚未取得藥物許可證（0 張登記），無法從許可證資料提取上市資訊。

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
Plummer-Vinson 症候群的病因即為缺鐵，鐵劑補充是機轉上最直接的介入手段，TxGNN 預測（99.94%）與現有臨床知識高度吻合。儘管本次 Evidence Pack 無直接臨床試驗或文獻收錄，機轉合理性極強，具備進一步評估的基礎。

**若要推進需要：**
- 補充 TFDA／香港衛生署（DH）仿單警語與禁忌資料（目前為 Blocking 缺口）
- 補充 DrugBank MOA 詳細資料，強化機轉分析
- 執行系統性文獻回顧，確認 Ferrous gluconate 與其他鐵劑在 PVS 治療的臨床報告
- 確認香港衛生署藥品許可證申請可行性（目前未上市）
- 評估其他 4 個預測適應症：
  - **Rank 2（巨母細胞貧血 B12/folate 獨立型）**：機轉連結弱，建議 Hold
  - **Rank 3（非症候群性食道畸形）**：先天性結構異常，建議 Hold
  - **Rank 4（生物素代謝疾病）**：無已知生化交叉點，建議 Hold
  - **Rank 5（維生素缺乏症，L3）**：有 4 個臨床試驗、2 篇文獻，值得作為研究課題追蹤
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

