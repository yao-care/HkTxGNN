---
layout: default
title: Rasagiline
parent: 僅模型預測 (L5)
nav_order: 759
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Rasagiline：預測新適應症為PLA2G6 相關神經退化症 (PLA2G6-associated neurodegeneration)（證據等級 L5）。原適應症：帕金森氏症（Parkinson disease）及相關帕金森症候群"
monitor_inn: "RASAGILINE"
predicted_indications: ["PLA2G6-associated neurodegeneration", "Rasmussen subacute encephalitis", "myelitis", "transaldolase deficiency"]
---

# Rasagiline
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

# Rasagiline：從帕金森氏症到 PLA2G6 相關神經退化症

## 一句話總結

Rasagiline 是一種選擇性、不可逆的 MAO-B 抑制劑，原本用於治療帕金森氏症及相關帕金森症候群。
TxGNN 模型預測它可能對 **PLA2G6 相關神經退化症 (PLA2G6-associated neurodegeneration)** 有效，
但目前**沒有任何臨床試驗或文獻**支持，僅屬模型預測階段。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 帕金森氏症（Parkinson disease）及相關帕金森症候群 |
| 預測新適應症 | PLA2G6 相關神經退化症 (PLA2G6-associated neurodegeneration) |
| TxGNN 預測分數 | 99.71% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 6 張 |
| 建議決策 | Hold |

註：香港許可證資料中未提供核准適應症文字，原適應症取自知識圖譜的適應症關聯。

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Rasagiline 是選擇性、不可逆的 MAO-B 抑制劑，可提高多巴胺的可用性，並被認為具有神經保護與抗細胞凋亡的特性。

PLA2G6 相關神經退化症包含嬰兒型神經軸突失養症，以及 PLA2G6 相關的肌張力不全－帕金森症 (PARK14)。其帕金森症狀表現與 Rasagiline 的原適應症有重疊，因此在**症狀層面**上，提升多巴胺可能帶來一定益處。

但沒有證據顯示 Rasagiline 能影響此疾病的根本病理（鐵沉積、脂質代謝缺陷、α-突觸核蛋白病變）。0.997 的高分很可能來自與帕金森相關適應症在知識圖譜中的網路鄰近性，而非直接證據。

### 其他預測適應症（供參考）

| 排名 | 預測疾病 | TxGNN 分數 | 評估 |
|------|---------|-----------|------|
| 2 | Rasmussen 亞急性腦炎 | 99.56% | 機轉上無明確關聯，可能是圖譜假象；MAO 抑制劑與抗癲癇藥、血清素類藥物有交互作用疑慮 |
| 3 | 脊髓炎 (myelitis) | 99.32% | 僅有前臨床神經保護作用，缺乏抗發炎或髓鞘再生證據，機轉推測性高 |
| 4 | 幼年型帕金森症 (paralysis agitans, juvenile, of Hunt) | 99.25% | 與現有適應症幾乎同義，並非真正的新適應症；幼年族群的安全性與療效未建立 |
| 5 | 轉醛醇酶缺乏症 | 99.19% | 與 MAO-B 抑制無明顯關聯，且 Rasagiline 經肝臟代謝 (CYP1A2)，肝臟受累族群需特別留意 |

以上各項皆無臨床試驗或文獻支持，證據等級均為 L5。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-67707 | RASAGILINE TABLETS 1MG | 錠劑（1mg） | 未提供 |
| HK-68563 | SINOREN TABLETS 1MG | 錠劑（1mg） | 未提供 |
| HK-60594 | AZILECT TAB 1MG | 錠劑（1mg） | 未提供 |
| HK-68329 | RASAGILINE GENEPHARM TABLETS 1MG | 錠劑（1mg） | 未提供 |
| HK-68530 | RASAGEN TABLETS 1MG | 錠劑（1mg） | 未提供 |

另有 HK-67847（RASAGILINA FARMOZ TABLETS 1MG），共 6 張許可證，皆為單方且有效。

---

## 安全性考量

- **知識圖譜標示的潛在禁忌疾病**（非仿單內容，僅供參考）：高血壓、多系統萎縮、姿勢性心搏過速症候群、姿勢性低血壓、藥物誘發運動困難、癲癇、雙極性疾患、重度情感性疾患、肝病、膽囊疾病、黑色素瘤、嗜鉻細胞瘤、十二指腸癌、小腸癌、心臟癌、腎上腺癌、交感神經副神經節瘤。
- **藥物交互作用**：共查得 100 筆，以下為部分範例。
  - **重大 (Major)**：Bupropion、Morphine
  - **中度 (Moderate)**：Epinephrine、Cimetidine、Phentermine、Diethylpropion、Dronabinol、Chlorpropamide、Glimepiride，以及多種胰島素（aspart、degludec、detemir、glargine、glulisine、human 等）

其餘警語與禁忌請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 5 個預測適應症皆無臨床試驗或文獻佐證，僅有模型預測（L5）。高分疑為網路鄰近性造成，並非直接證據。
- 排名 1 的 PLA2G6 相關神經退化症，僅在帕金森症狀層面有合理推測，對疾病本身進程無證據。

**若要推進需要：**
- 取得香港衛生署仿單，確認警語、禁忌與核准適應症（目前為阻擋性資料缺口）
- 補充詳細的作用機轉（MOA）資料
- 針對 PLA2G6 相關神經退化症（尤其 PARK14 表型）進行文獻與病例回顧，並設計前臨床或小型探索性研究
- 評估兒童與青少年族群的安全性與劑量
- 排名 4 的幼年型帕金森症應視為既有適應症的同義詞，不列為新適應症
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

