---
layout: default
title: Sertaconazole
parent: 僅模型預測 (L5)
nav_order: 809
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Sertaconazole：預測新適應症為體癬 (Tinea Corporis)（證據等級 L5）。原適應症：足癬（Tinea pedis）。香港許可證未提供核准適應症文字，此為知識圖譜資料"
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

# Sertaconazole：從足癬到體癬

## 一句話總結

Sertaconazole 是咪唑類（imidazole）外用抗黴菌藥，原本用於足癬（tinea pedis）。
TxGNN 模型預測它可能對**體癬 (Tinea Corporis)** 有效，
目前有 **0 個已登記臨床試驗**和 **20 篇文獻**支持這個方向，其中包含多項隨機對照比較研究。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 足癬（Tinea pedis）。香港許可證未提供核准適應症文字，此為知識圖譜資料 |
| 預測新適應症 | 體癬 (Tinea Corporis) |
| TxGNN 預測分數 | 99.94% |
| 證據等級 | L1（依已發表文獻判定，試驗階段與盲性未逐一確認，屬暫定） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 2 張 |
| 建議決策 | Proceed with Guardrails |

> 說明：TxGNN 分數最高的預測為「腹股溝及肛周皮癬（體股癬）」（99.98%），但該項目沒有任何臨床試驗或文獻，證據等級為 L5。本報告以證據最完整的「體癬」為主要評估對象，其他預測見文末附表。

---

## 為什麼這個預測合理？

目前缺乏 DrugBank 的詳細作用機轉資料。根據文獻，Sertaconazole 是咪唑類抗黴菌藥，透過抑制麥角固醇（ergosterol）合成（抑制 lanosterol 14-α-demethylase）發揮作用。其苯并噻吩（benzothiophene）基團還能直接與真菌細胞壁的非固醇脂質結合，增加膜通透性，高濃度時可造成真菌死亡。

體癬與足癬同屬皮癬菌（dermatophyte）感染，致病菌相近，給藥途徑同為外用。機轉相同，因此預測在機轉上合理。這比較接近「適應症擴增」（label extension），而非真正跨疾病的藥物再利用。

多項隨機比較研究（對照 terbinafine、clotrimazole、butenafine、eberconazole 等）已在局部體癬與股癬中評估其療效與安全性。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

以下為與體癬或皮癬菌感染最相關的文獻（優先列出 RCT）：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [35068526](https://pubmed.ncbi.nlm.nih.gov/35068526/) | 2021 | RCT | Indian J Dermatol | Eberconazole 與 Sertaconazole 用於局部皮癬感染的療效與安全性比較 |
| [24249898](https://pubmed.ncbi.nlm.nih.gov/24249898/) | 2013 | RCT | Indian J Dermatol | Terbinafine 1% 與 Sertaconazole 2% 乳膏用於體癬與股癬的比較試驗 |
| [18039020](https://pubmed.ncbi.nlm.nih.gov/18039020/) | 2007 | RCT | Am J Clin Dermatol | 2% 溶液與乳膏劑型用於體癬、趾間足癬或相應念珠菌病的比較；結論為安全有效 |
| [25386455](https://pubmed.ncbi.nlm.nih.gov/25386455/) | 2014 | RCT | J Clin Diagn Res | Sertaconazole 與 Clotrimazole 治療體癬的比較 |
| [24249897](https://pubmed.ncbi.nlm.nih.gov/24249897/) | 2013 | RCT | Indian J Dermatol | 2% Sertaconazole 與 1% Butenafine 在皮膚癬感染的開放標籤比較（含成本效益） |
| [17121064](https://pubmed.ncbi.nlm.nih.gov/17121064/) | 2006 | RCT | Cutis | 兩項雙盲、載體對照研究（383 人隨機分組），足癬 4 週黴菌學治癒率達 70.3%（針對原適應症） |
| [30409926](https://pubmed.ncbi.nlm.nih.gov/30409926/) | 2019 | 隨機雙盲試驗 | Indian J Dermatol Venereol Leprol | Amorolfine 0.25% 與 Sertaconazole 2% 乳膏用於局限性皮癬 |
| [28066103](https://pubmed.ncbi.nlm.nih.gov/28066103/) | 2016 | 隨機觀察者盲 | Indian J Pharmacol | 每日一次 Sertaconazole 與 Terbinafine 用於局部皮癬的比較 |
| [34760651](https://pubmed.ncbi.nlm.nih.gov/34760651/) | 2021 | 隨機開放標籤 | Perspect Clin Res | Sertaconazole 與 Luliconazole 乳膏在皮癬的療效、安全與成本效益比較 |
| [19275277](https://pubmed.ncbi.nlm.nih.gov/19275277/) | 2009 | Review | Drugs | 在皮膚科與婦科淺部黴菌症的使用回顧；歐盟適應症涵蓋體癬、股癬、足癬等，美國僅核准足癬 |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-50619 | ZALAIN CREAM 2% | 乳膏（依品名） | 未提供 |
| HK-51145 | ZALAIN VAGINAL SUPP 300MG | 陰道栓劑（依品名） | 未提供 |

兩張許可證均為單方、有效，持有人為 LEON MEDICAL SUPPLIES LIMITED。

---

## 安全性考量

安全性資訊請參考原廠仿單。目前未查得藥物交互作用資料。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 體癬與已核准的足癬同屬皮癬菌感染，機轉與外用途徑相同，且有多項隨機對照比較研究支持。
- 但現有研究多為小型、開放標籤、以活性藥物對照的研究，集中於少數地區，且無登記試驗。

**若要推進需要：**
- 取得 DrugBank 作用機轉資料與香港仿單（警語、禁忌）。
- 確認各研究的試驗階段、盲性與樣本數，必要時重新評估證據等級。
- 確認香港許可證核准的適應症範圍（目前未提供）。

---

## 附錄：其他預測適應症概覽

| 預測適應症 | TxGNN 分數 | 證據等級 | 建議 | 備註 |
|-----------|-----------|---------|------|------|
| 腹股溝及肛周皮癬 | 99.98% | L5 | Hold | 無試驗或文獻，僅有模型預測 |
| 皮膚念珠菌症 | 99.63% | L2 | Proceed with Guardrails | 僅有早期 Phase II 研究與小型兒童研究 |
| 淺部黴菌症 | 99.55% | L2 | Proceed with Guardrails | 證據來自各亞型彙整，使用前需先界定亞型 |
| 頭皮或鬍鬚皮癬 | 99.55% | L4 | Hold | 僅有回顧與體外研究；毛囊感染外用通常不足 |
| 花斑癬 (Pityriasis versicolor) | 99.45% | L3 | Research Question | 僅有一項 1992 年小型研究 |
| 外毛癬、內毛癬、Majocchi 肉芽腫、深部癬 | 99.37–99.59% | L5 | Hold | 無臨床證據；毛囊或深部感染通常需全身治療 |
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

