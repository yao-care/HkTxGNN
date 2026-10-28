---
layout: default
title: Mirtazapine
parent: 僅模型預測 (L5)
nav_order: 591
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-14
monitor_inn: "MIRTAZAPINE"
predicted_indications: ["Ohdo syndrome and variants", "blepharophimosis - intellectual disability syndrome, Ohdo type", "benign paroxysmal torticollis of infancy"]
description: "Mirtazapine：預測新適應症為Ohdo 症候群及其變異型 (Ohdo syndrome and variants)（證據等級 L5）。原適應症：本地許可證資料未記載適應症"
---

# Mirtazapine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

## Mirtazapine: Ohdo 症候群及其變異型 (Ohdo syndrome and variants)
{: .text-alpha }

## 一句話總結

Mirtazapine 是一種抗憂鬱藥物，原本用於憂鬱症（含單極性憂鬱、內因性憂鬱、重度憂鬱症）與焦慮症的治療。
TxGNN 模型預測它可能對 **Ohdo 症候群及其變異型 (Ohdo syndrome and variants)** 有效，
但目前**沒有任何臨床試驗或文獻**支持，僅有模型預測分數。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本地許可證資料未記載適應症 |
| 預測新適應症 | Ohdo 症候群及其變異型 (Ohdo syndrome and variants) |
| TxGNN 預測分數 | 0.9942 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 20 張／共 20 張） |
| 許可證數 | 20 張（有效 20 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Mirtazapine 一般已知為 alpha-2 腎上腺素受體、5-HT2、5-HT3 及 H1 受體的拮抗劑，其療效在憂鬱症與焦慮症中已被廣泛使用，但這些資訊並非來自本報告所彙整的機轉欄位，僅作背景參考。

Ohdo 症候群及其變異型是一種罕見的遺傳性疾病，常與 KAT6B 基因變異相關，特徵為智能障礙與眼瞼狹小。就現有資料而言，無法建立 mirtazapine 的受體藥理與此疾病病理之間的合理關聯。此預測分數來自 TxGNN 模型（深度學習），較可能反映模型從相關疾病之間學到的相似性，而非經驗證的生物學證據或機轉。

即使有任何益處，也可能僅限於改善伴隨的情緒、睡眠或食慾問題等次要症狀，並非疾病修飾作用。另外，本次預測排名第 2 的「blepharophimosis - intellectual disability syndrome, Ohdo type」（分數 0.9911）與此項高度重疊，兩者不應視為獨立證據。排名第 3 為嬰兒良性陣發性斜頸（分數 0.9911），同樣無任何研究支持，且對嬰幼兒使用具鎮靜作用的抗憂鬱藥風險效益比不佳。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-66562 | MIRTA ORODISPERSIBLE TABLETS 30MG | 口溶錠（依品名） | 未提供 |
| HK-52381 | REMERON SOLTAB ORODISPERSIBLE TAB 15MG | 口溶錠（依品名） | 未提供 |
| HK-67333 | MIRZENTAC TABLETS 30MG | 錠劑（依品名） | 未提供 |
| HK-53225 | PMS-MIRTAZAPINE TAB 30MG | 錠劑（依品名） | 未提供 |
| HK-56412 | PMS-MIRTAZAPINE TAB 15MG | 錠劑（依品名） | 未提供 |

以上僅列出 5 張主要許可證，全部 20 張皆為有效的單方許可證，無已註銷者。

## 安全性考量

- **知識圖譜標示的禁忌疾病**（來自知識圖譜關聯，非仿單文字）：癲癇、躁期雙極性情感障礙、肝病、膽囊疾病、嗜中性白血球低下、顆粒球缺乏症、姿位性低血壓、低血壓疾病、高三酸甘油脂血症、肥胖、中風及腦血管疾病、腦梗塞、心肌梗塞、冠狀動脈血栓、血紅素病變、腎功能不全、血清素症候群、藥物引起的靜坐不能，以及多系統萎縮症與姿勢性直立心搏過速症候群。
- **藥物交互作用**：共查得 100 筆，以下為部分範例：
  - 嚴重 (Major)：Bupropion、Lorcaserin、Dolasetron、Palonosetron
  - 中度 (Moderate)：Famotidine、Loperamide、Aprepitant、Morphine、Dexamethasone、Cimetidine、Clarithromycin、Levofloxacin 等
- **兒童族群**：抗憂鬱藥在年輕族群有自殺風險的警語，且 mirtazapine 未獲准用於兒童。

其餘警語與禁忌資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 支持此預測的證據僅有 TxGNN 模型分數，無任何臨床試驗或文獻，證據等級為 L5。
- 無法建立合理的機轉關聯，且前三名預測互有重疊、並非獨立證據；就罕見遺傳疾病而言，使用此藥僅可能緩解次要症狀。

**若要推進需要：**
- 取得完整的作用機轉資料，並評估與 KAT6B 相關病理的可能關聯
- 取得香港衛生署的仿單警語與禁忌資訊，完成安全性篩選
- 進行文獻與臨床試驗的系統性檢索，確認是否有任何前臨床或病例報告支持
- 若有意探索，應先定義具體的症狀性目標（如睡眠、情緒、食慾），並另行評估證據
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

