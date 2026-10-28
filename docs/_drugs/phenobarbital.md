---
layout: default
title: Phenobarbital
parent: 僅模型預測 (L5)
nav_order: 688
evidence_level: L5
indication_count: 3
monitor_inn: "PHENOBARBITAL"
predicted_indications: ["trigeminal nerve neoplasm", "trigeminal neuralgia", "beta-ketothiolase deficiency"]
last_modified_at: 2026-10-23
description: "Phenobarbital：預測新適應症為三叉神經腫瘤 (Trigeminal Nerve Neoplasm)（證據等級 L5）。原適應症：香港許可證未載明核准適應症文字"
---

# Phenobarbital
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

## Phenobarbital：從癲癇到三叉神經腫瘤
{: .text-alpha }

## 一句話總結

Phenobarbital（苯巴比妥）是長期使用的巴比妥類抗癲癇藥，知識圖譜中記錄的相關用途以癲癇與偏頭痛類疾病為主。
TxGNN 模型預測它可能對**三叉神經腫瘤 (Trigeminal Nerve Neoplasm)** 有效，但目前**沒有任何臨床試驗**，僅有 **1 篇**不直接相關的文獻（Sturge-Weber 症候群病例系列），證據非常薄弱。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 香港許可證未載明核准適應症文字；知識圖譜中記錄的相關疾病包括癲癇、偏頭痛、Lennox-Gastaut 症候群等 |
| 預測新適應症 | 三叉神經腫瘤 (Trigeminal Nerve Neoplasm) |
| TxGNN 預測分數 | 0.9996 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 4 張／共 4 張） |
| 許可證數 | 4 張（有效 4 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。一般已知 Phenobarbital 是 GABA-A 受體的正向異位調節劑，可增強抑制性神經傳導、抑制神經元過度興奮，因此用於癲癇控制。

然而，這種機轉與抗腫瘤作用沒有已知的關聯。Phenobarbital 對三叉神經腫瘤沒有已知的抗腫瘤活性。唯一檢索到的文獻談的是 Sturge-Weber 症候群（一種伴隨癲癇的神經皮膚血管疾病），並非腫瘤。因此這個高分預測的分數來自 TxGNN 模型（深度學習），可能反映模型學到的相關疾病之間的相似性，並非生物學證據。最多只能推測它可用於處理腫瘤相關癲癇，屬於症狀控制，並非治療腫瘤本身。

另外兩個預測（三叉神經痛、β-酮硫解酶缺乏症）同樣缺乏直接證據：前者的文獻多半在談 carbamazepine，後者則沒有任何研究。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [9157801](https://pubmed.ncbi.nlm.nih.gov/9157801/) | 1997 | 病例系列 | Anales espanoles de pediatria | 回顧 14 例 Sturge-Weber 症候群的臨床特徵與治療反應；該病不是腫瘤，與預測疾病無直接關聯 |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-43727 | UNI-FENO SYRUP 15MG/5ML | 未載明 | 未載明 |
| HK-45682 | PHENOBARBITONE SOD. INJ 200MG/ML | 未載明 | 未載明 |
| HK-04992 | PHENOBARBITONE TAB 60MG | 未載明 | 未載明 |
| HK-04966 | PHENOBARBITONE TAB 30MG | 未載明 | 未載明 |

## 安全性考量

- **知識圖譜中記錄的禁忌關聯（非仿單內容）**：高血壓、肝衰竭／肝病、慢性阻塞性肺病、卟啉症、腎臟病、血小板低下、高血糖、甲狀腺功能低下、消化性潰瘍、全身性紅斑狼瘡、精神疾病等。
- **藥物交互作用**（共查得 100 筆，以下為部分）：
  - 嚴重 (Major)：Morphine、Morphine（脂質體）、Eliglustat、Naldemedine、Naloxegol、Rolapitant
  - 中度 (Moderate)：Doxycycline、Hydrocortisone、Dexamethasone、Prednisone、Pioglitazone、Bupropion、Aprepitant、Metronidazole 等

詳細警語與禁忌請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 預測分數雖高，但屬於網絡推論；沒有臨床試驗，也沒有直接研究三叉神經腫瘤的文獻，且機轉上無合理的抗腫瘤依據，證據等級僅為 L5。

**若要推進需要：**
- 取得直接探討 Phenobarbital 與三叉神經腫瘤的研究證據
- 補充作用機轉資料，並評估是否僅能作為腫瘤相關癲癇的症狀處理
- 取得香港許可證的核准適應症與仿單警語、禁忌
- 若轉向「三叉神經痛」，需有 Phenobarbital 專屬的對照研究，並與 carbamazepine 等既有選擇比較，同時評估其酵素誘導造成的交互作用與鎮靜、依賴風險
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

