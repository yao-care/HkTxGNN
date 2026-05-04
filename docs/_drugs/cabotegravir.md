---
layout: default
title: Cabotegravir
parent: 僅模型預測 (L5)
nav_order: 121
evidence_level: L5
indication_count: 5
---

# Cabotegravir
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

# Cabotegravir：從 HIV 到類風濕性關節炎

## 一句話總結

Cabotegravir 是一種 HIV 整合酶股轉移抑制劑（INSTI），用於 HIV-1 的治療與暴露前預防（PrEP）。TxGNN 模型預測它可能對**類風濕性關節炎 (Rheumatoid Arthritis)** 有效，預測分數高達 99.45%。然而，目前**無任何臨床試驗或文獻**支持此方向，所有證據均來自模型預測，建議暫緩推進。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | HIV-1 感染治療與暴露前預防（PrEP） |
| 預測新適應症 | 類風濕性關節炎 (Rheumatoid Arthritis) |
| TxGNN 預測分數 | 99.45% |
| 證據等級 | L5 |
| 台灣上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（MOA 資料缺失）。根據已知資訊，Cabotegravir 屬於 HIV 整合酶股轉移抑制劑（INSTI），透過抑制 HIV 整合酶阻止病毒 DNA 嵌入宿主基因組，從而阻斷 HIV 複製週期。台灣目前尚無核准許可，但此藥在多國以長效注射劑型（每月或每兩個月一次）上市。

然而，Cabotegravir 與類風濕性關節炎（RA）的機轉關聯性**極弱**。RA 的自體免疫病理主要涉及 Th17／TNF-α／IL-6 炎症軸，與 HIV 整合酶抑制無已知直接連結。部分 INSTI 類藥物曾有輕微抗炎效應的零星觀察（透過 NF-κB 旁路抑制），但目前尚無針對 RA 靶點的明確機轉假說，相關研究幾乎空白。

TxGNN 給出高預測分數的最可能原因，是知識圖譜中 **HIV 患者合併 RA 的流行病學共病節點關聯**——HIV 感染者因免疫失調，RA 共病率略高於一般族群，這種流行病學訊號被圖譜學習後轉化為高分預測，屬於**相關性驅動而非機轉驅動**的結果，需謹慎解讀。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 台灣上市資訊

Cabotegravir 目前**未在台灣取得藥品許可證**，無任何核准上市紀錄。若未來有再利用研究需求，需先確認在台的試驗用藥申請（IND）流程。

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 與類風濕性關節炎的機轉關聯性極弱，TxGNN 高分很可能來自流行病學共病訊號，而非藥理機轉支撐
- 無任何臨床試驗或文獻支持此再利用方向，屬純模型預測（L5），風險效益比尚無從評估

**若要推進需要：**
- 補充完整的作用機轉資料（DrugBank MOA、整合酶抑制與免疫調節的交叉研究）
- 取得台灣藥品仿單全文，釐清警語與禁忌症（目前為資料缺口）
- 確認 INSTI 類藥物對 NF-κB 或 RA 相關炎症通路是否有前臨床研究支持
- 考慮以系統性回顧方式評估 HIV 患者長期使用 Cabotegravir 後 RA 發病率的真實世界數據，以辨別共病關聯是否具有治療意涵

---

> ⚠️ **免責聲明**：本報告僅供研究參考，不構成醫療建議。老藥新用候選需經臨床驗證方可應用於臨床實踐。
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

