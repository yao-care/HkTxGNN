---
layout: default
title: Cetrorelix
parent: 僅模型預測 (L5)
nav_order: 156
evidence_level: L5
indication_count: 10
---

# Cetrorelix
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

# Cetrorelix：從輔助生殖到多毛症

## 一句話總結

Cetrorelix 是一種競爭性 GnRH 受體拮抗劑，已在歐美等多國核准用於輔助生殖技術（IVF），預防卵巢刺激期間的早發性 LH 峰，香港目前尚未上市。
TxGNN 模型預測它可能對**多毛症 (Hypertrichosis)** 有效（預測分數 99.98%），但目前**無任何臨床試驗或直接文獻**支持此方向，機轉連結存在根本性疑問，建議暫緩推進。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 輔助生殖技術（IVF）中預防早發性 LH 峰（國際核准適應症，香港未上市） |
| 預測新適應症 | 多毛症 (Hypertrichosis) |
| TxGNN 預測分數 | 99.98% |
| 證據等級 | L5 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（本次 Evidence Pack 標記為資料缺口）。根據已知藥理資訊，Cetrorelix 為合成十肽 GnRH 受體拮抗劑，競爭性阻斷下視丘 GnRH 受體，快速且可逆地抑制腦垂體分泌 LH 與 FSH，進而降低卵巢及睪丸性激素（雌激素、睪固酮）水平，此機轉為輔助生殖療效的核心基礎。

多毛症（Hypertrichosis）分為兩大臨床類型。第一類為雄激素依賴性多毛症（hirsutism），由高雄激素驅動毛囊過度生長；理論上 Cetrorelix 透過抑制 LH→睪固酮路徑，可能對此亞型有部分調節效果。第二類為真性多毛症（true hypertrichosis），成因為遺傳突變（如 Ambras 症候群的 8q22 染色體重排）、藥物誘發或全身性疾病，與 GnRH-HPG 軸完全無關，Cetrorelix 的作用標靶無法覆蓋此機轉。

ICD 分類的廣義「hypertrichosis (disease)」同時涵蓋上述兩類病因，TxGNN 知識圖譜的預測可能源自 GnRH 系統與毛囊雄激素路徑間的間接節點連結，高分預測並不代表直接藥理對應。在未細分亞型的前提下，本預測的生物合理性有限。

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
TxGNN 預測分數雖高（99.98%），但多毛症為廣義診斷，多數亞型（如遺傳性毛幹結構異常、Ambras 症候群、睫毛過長症）與 GnRH 軸無直接機轉關聯；目前完全無臨床試驗或文獻直接支持此再利用方向，屬 L5 最低證據等級。此外 Cetrorelix 香港未上市，且警語、禁忌等安全性資料存在關鍵缺口，目前無法進入安全性初評（S1）。

**若要推進需要：**
- 明確區分多毛症亞型，聚焦**雄激素依賴性亞群（hirsutism）**作為機轉更合理的切入點，並重新評估該亞型的 TxGNN 預測結果
- 補充 Cetrorelix 作用機轉正式文獻（DrugBank MOA 欄位）
- 取得香港藥監局資料或原廠仿單，填補警語與禁忌資料缺口以完成安全性初評
- 進行前臨床探索性研究，建立 GnRH 拮抗劑對雄激素依賴性多毛症的基礎藥理證據
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

