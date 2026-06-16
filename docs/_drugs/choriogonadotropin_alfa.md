---
layout: default
title: Choriogonadotropin Alfa
parent: 僅模型預測 (L5)
nav_order: 166
evidence_level: L5
indication_count: 10
---

# Choriogonadotropin Alfa
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Choriogonadotropin Alfa：從輔助生殖到消化性食道炎

## 一句話總結

Choriogonadotropin alfa 是重組人類絨毛膜促性腺激素（recombinant hCG），臨床上主要用於輔助生殖技術（ART）中誘導卵泡最終成熟與排卵。TxGNN 模型預測它可能對**消化性食道炎 (Peptic Esophagitis)** 有效，預測分數高達 98.44%，但目前**無任何臨床試驗或文獻**支持此方向，此預測可能源於知識圖譜中的非特異性節點連結，而非真實的生物學相關性。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 輔助生殖技術（ART）：誘導卵泡成熟、觸發排卵、黃體支持 |
| 預測新適應症 | 消化性食道炎 (Peptic Esophagitis) |
| TxGNN 預測分數 | 98.44% |
| 證據等級 | L5 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（MOA 為資料缺口）。根據已知藥理資訊，Choriogonadotropin alfa 是以重組 DNA 技術製造的 hCG，透過結合黃體生成素／絨毛膜促性腺激素受體（LHCGR），刺激卵巢卵泡最終成熟與黃體生成；在男性則促進睾丸間質細胞（Leydig cells）分泌睾固酮，屬典型的生殖系統荷爾蒙藥物。

就機轉關聯性而言，消化性食道炎的核心病理是胃酸逆流造成的食道黏膜損傷，與 hCG 的促性腺作用並無直接交集。更關鍵的是，LHCGR 在消化道（包括食道）的表現極為稀少，目前無已知機轉支持促性腺激素對食道發炎具有直接療效。

此預測雖獲得高分（98.44%），但機轉分析顯示這很可能是知識圖譜的假陽性訊號：「消化性食道炎」作為 KG 中連結廣泛的節點，可能因拓撲結構而與多個無生物學關聯的藥物產生高分預測。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
LHCGR 在食道黏膜幾乎不表現，消化性食道炎的病理機制（胃酸損傷）與 hCG 的生殖荷爾蒙作用路徑無合理交集；在完全缺乏前臨床與臨床佐證的情況下（L5 等級），此預測不具備足夠的科學依據支持進一步投入。

**若要推進需要：**
- 基礎研究確認 LHCGR 是否在食道黏膜有功能性表現
- 機轉假說的前臨床驗證（細胞株或動物食道炎模型）
- 補齊 MOA 完整資料（建議查詢 DrugBank API：DB00097）
- 補齊香港仿單警語與禁忌症資料（TFDA/衛署藥准字 PDF 解析）
- 確認給藥途徑可行性（hCG 目前為注射劑型，用於消化道疾病需評估全身暴露的合理性）
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

