---
layout: default
title: Tramadol
parent: 僅模型預測 (L5)
nav_order: 878
evidence_level: L5
indication_count: 10
---

# Tramadol
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

# Tramadol：從鎮痛用途到肢中段發育不良（Hunter-Thompson 型）

## 一句話總結

Tramadol 是一種鎮痛藥，作用於 mu 類鴉片受體並抑制單胺再吸收。
TxGNN 模型預測它可能對**肢中段發育不良 Hunter-Thompson 型 (Acromesomelic dysplasia, Hunter-Thompson type)** 有效。
目前**沒有臨床試驗，也沒有文獻**支持，僅有模型預測，不建議推進。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 肢中段發育不良 Hunter-Thompson 型 (Acromesomelic dysplasia, Hunter-Thompson type) |
| TxGNN 預測分數 | 99.99% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Tramadol 的已知作用是 mu 類鴉片受體促效與單胺再吸收抑制，這些作用最多只能帶來症狀性的止痛。

這個新適應症是罕見的骨骼發育異常，成因是影響骨與軟骨生長訊號的基因缺陷。Tramadol 對這些病因路徑沒有已知作用，無法改變疾病本身。

TxGNN 分數約 0.9999，已趨近飽和，單憑分數無法說明預測的可信度。目前看不出合理的機轉關聯，此預測只是知識圖譜上的推論。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

| 許可證號 | 品名 | 製造商 |
|---------|------|--------|
| HK-58224 | TRADOLGESIC CAP 50MG | TRENTON-BOMA LTD |
| HK-66387 | MYOTRAM 100 SOLUTION FOR INJECTION/INFUSION 100MG/2ML | HANG LUNG TRADING (H.K.) CO |
| HK-35707 | MABRON CAP 50MG | STAR MEDICAL SUPPLIES LTD |
| HK-44533 | SEFMAL CAP 50MG | HEALTH ALLIANCE INTERNATIONAL CO LTD |
| HK-41704 | TRAMADOL 50 STADA CAP 50MG | STADA PHARMACEUTICALS (ASIA) LIMITED |

此資料來源未提供這些許可證的核准適應症文字與劑型。

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 沒有任何臨床試驗或文獻，證據等級僅為 L5。
- 機轉上沒有合理的疾病修飾作用，高分只反映模型的飽和輸出。
- 同一份預測清單的其餘 9 個候選（骨骼發育異常、幼年型關節炎、類風濕結節等）同樣是 L5、Hold。
- 其中幼年型特發性關節炎 (JIA) 的兩篇文獻並未評估 tramadol，也不能支持此預測。

**若要推進需要：**
- 取得 Tramadol 的作用機轉資料（DrugBank）。
- 取得香港衛生署仿單的警語與禁忌資料，完成安全性篩選。
- 找到疾病模型或機轉層面的前臨床證據，說明 Tramadol 如何影響此疾病的病因路徑。
- 若僅是症狀性止痛，這屬於既有用途，不應視為老藥新用。

*本報告僅供研究參考，不構成醫療建議。預測結果需經臨床驗證。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

