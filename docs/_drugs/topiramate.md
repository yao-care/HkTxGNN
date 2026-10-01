---
layout: default
title: Topiramate
parent: 僅模型預測 (L5)
nav_order: 875
evidence_level: L5
indication_count: 5
---

# Topiramate
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

# Topiramate：從癲癇到三叉神經腫瘤

## 一句話總結

Topiramate 是一種抗癲癇藥，香港許可證資料中未載明原適應症。
TxGNN 模型預測它可能對**三叉神經腫瘤 (Trigeminal Nerve Neoplasm)** 有效，但目前**沒有任何臨床試驗或文獻**支持，這只是模型的圖譜預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 許可證未載明（文獻顯示為抗癲癇藥） |
| 預測新適應症 | 三叉神經腫瘤 (Trigeminal Nerve Neoplasm) |
| TxGNN 預測分數 | 99.70% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據其他資料，Topiramate 具有多重抗癲癇機轉：阻斷電壓門控鈉離子通道、增強 GABA-A 活性、抑制 AMPA/kainate 受體。

這些機轉都屬於神經興奮性調節，與腫瘤生物學沒有已知的關聯。模型給出高分，很可能是知識圖譜把「三叉神經」相關的神經學詞彙（如三叉神經痛、頭痛）連結到腫瘤節點所造成的假象，而不是真實的藥理關聯。

因此，這個預測目前沒有機轉層面的支持，不建議把高分視為療效訊號。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

下列為 20 張許可證中的 5 張，許可證資料未提供劑型與核准適應症。

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-68292 | TORATE 25 TABLETS 25MG | HANG LUNG TRADING (H.K.) CO |
| HK-63959 | TOPIRAMATE SANDOZ TABLET 50MG | SANDOZ HONG KONG LIMITED |
| HK-55963 | APO-TOPIRAMATE TAB 25MG | HIND WING CO LTD |
| HK-65187 | TORAMAT TABLETS 50MG | I & C (HONG KONG) LIMITED |
| HK-64179 | TOPIRAMATE TABLETS 50MG | HONG KONG MEDICAL SUPPLIES LTD |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
這個適應症只有模型預測分數（證據等級 L5），沒有臨床試驗、文獻，也沒有合理的機轉連結，不具備推進的依據。

**若要推進需要：**
- 補齊 Topiramate 的作用機轉資料（DrugBank）
- 取得香港衞生署仿單的警語與禁忌症
- 找出 Topiramate 與三叉神經腫瘤之間的前臨床或機轉證據，以排除知識圖譜假象
- 若要在此藥上找較有潛力的方向，同一份預測中排名第 2 的**視覺性癲癇 (Visual Epilepsy)** 證據等級為 L2，有 Phase 3 試驗與多篇系統性回顧，值得另案評估。但癲癇本身已是該藥的既有用途，再利用價值僅限於亞型定位。

> 本報告僅供研究參考，不構成醫療建議。老藥新用候選需經過臨床驗證才能應用。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

