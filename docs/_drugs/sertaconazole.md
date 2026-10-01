---
layout: default
title: Sertaconazole
parent: 僅模型預測 (L5)
nav_order: 794
evidence_level: L5
indication_count: 10
---

# Sertaconazole
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

# Sertaconazole：從淺部黴菌感染到腹股溝及肛周皮癬菌病

## 一句話總結

Sertaconazole 是咪唑類（imidazole）外用抗黴菌藥，依文獻原本用於淺部皮膚與黏膜黴菌感染。
TxGNN 模型預測它可能對**腹股溝及肛周皮癬菌病 (Dermatophytosis of groin and perianal area)** 有效，但目前**沒有任何臨床試驗或文獻**直接支持這個適應症，僅有模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 香港許可證未載明；依文獻為淺部皮膚黴菌與念珠菌感染 |
| 預測新適應症 | 腹股溝及肛周皮癬菌病 (Dermatophytosis of groin and perianal area) |
| TxGNN 預測分數 | 99.98% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 2 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（DrugBank 的 MOA 欄位為空）。不過從文獻可知，Sertaconazole 是咪唑類抗黴菌藥，抑制 14-α lanosterol demethylase，阻斷麥角固醇（ergosterol）合成。它的苯并噻吩環還可能直接在黴菌細胞膜上造成孔洞。這些機轉都與皮癬菌（dermatophyte）的感染生物學相符。

腹股溝及肛周皮癬菌病和體癬（tinea corporis）是同一類皮癬菌感染，只是發生部位不同，皮膚環境也相近。因此模型給出很高的分數是合理的。

要注意兩點：
- 針對此部位本身，沒有檢索到任何試驗或文獻，所以目前只能說機轉合理，不能說有證據。
- 同一份資料中，體癬及局部皮癬菌病有多項 Sertaconazole 的隨機對照試驗，其中至少兩項納入股癬（tinea cruris）病人（PMID 24249898、28066103）。這可作為間接佐證，但仍需針對腹股溝部位另做文獻檢索確認。

**同一藥物的其他預測適應症（供比較）**

| 預測適應症 | 證據等級 | 建議 |
|-----------|---------|------|
| 體癬 (Tinea corporis) | L1 | Proceed with Guardrails |
| 皮膚念珠菌病 (Cutaneous candidiasis) | L2 | Proceed with Guardrails |
| 淺部黴菌病 (Superficial mycosis) | L2 | Proceed with Guardrails |
| 花斑癬 (Pityriasis versicolor) | L3 | Research Question |
| 頭皮或鬍鬚皮癬菌病 | L4 | Hold |
| 毛外型／毛內型感染、Majocchi 肉芽腫、深部癬 (Tinea profunda) | L5 | Hold |

體癬的證據最完整，且 Sertaconazole 本來就用於淺部黴菌感染，接近於適應症內使用，而非嚴格意義上的老藥新用。

## 臨床試驗證據

目前無相關臨床試驗登記

## 文獻證據

目前無相關文獻

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-50619 | ZALAIN CREAM 2% | 乳膏（依品名） | 資料未載明 |
| HK-51145 | ZALAIN VAGINAL SUPP 300MG | 陰道栓劑（依品名） | 資料未載明 |

兩張許可證的持有者皆為 LEON MEDICAL SUPPLIES LIMITED。乳膏為外用劑型，與皮膚黴菌感染的使用途徑相符。

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 針對腹股溝及肛周皮癬菌病，沒有任何臨床試驗或文獻，僅有 TxGNN 預測（證據等級 L5）。
- 同一藥物在體癬等相近適應症有較完整的證據（體癬為 L1），這個方向值得優先評估。

**若要推進需要：**
- 針對股癬（tinea cruris）和肛周皮癬菌病，做專門的文獻與試驗檢索，確認 PMID 24249898、28066103 等研究的股癬受試者數據。
- 取得香港衛生署核准的仿單，確認原適應症、警語與禁忌症。
- 補充 DrugBank 的作用機轉資料。
- 確認給藥途徑相容性（目前狀態待確認）。

*本報告僅供研究參考，不構成醫療建議。預測結果需經臨床驗證後才能應用。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

