---
layout: default
title: Tioconazole
parent: 僅模型預測 (L5)
nav_order: 880
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-14
description: "Tioconazole：預測新適應症為外陰陰道炎 (Vulvovaginitis)（證據等級 L1）。原適應症：外陰陰道念珠菌病 (Vulvovaginal candidiasis)"
monitor_inn: "TIOCONAZOLE"
predicted_indications: ["vulvovaginitis", "vulvitis", "postmenopausal atrophic vaginitis"]
---

# Tioconazole
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

## Tioconazole：從外陰陰道念珠菌病到外陰陰道炎
{: .text-alpha }

## 一句話總結

Tioconazole 是咪唑類（imidazole）抗黴菌藥，原本用於外陰陰道念珠菌病。
TxGNN 模型預測它可能對**外陰陰道炎 (Vulvovaginitis)** 有效，
目前有 **19 篇文獻**支持這個方向（無臨床試驗登記），但實質上這幾乎等同於原適應症，僅是標籤範圍較廣。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 外陰陰道念珠菌病 (Vulvovaginal candidiasis) |
| 預測新適應症 | 外陰陰道炎 (Vulvovaginitis) |
| TxGNN 預測分數 | 0.9923 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 4 張／共 4 張） |
| 許可證數 | 4 張（有效 4 張） |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料庫記載，但此類藥物的機轉已相當明確：Tioconazole 抑制真菌的羊毛固醇 14-α 去甲基酶（CYP51/ERG11），阻斷麥角固醇（ergosterol）合成，破壞真菌細胞膜完整性。此外，它也會抑制人類的 CYP8B1 酵素（參與膽酸合成路徑的一個分支）。

外陰陰道炎多數由念珠菌屬引起，因此這個預測實質上等同於已確立的適應症（外陰陰道念珠菌病），只是疾病名稱較廣泛。

需要注意的是，對於非念珠菌性的外陰陰道炎（細菌性、滴蟲性、萎縮性或刺激性），並沒有證據支持其療效。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

下表列出最相關的 10 篇（優先 RCT，其次為綜述與臨床研究）：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [3524439](https://pubmed.ncbi.nlm.nih.gov/3524439/) | 1986 | RCT | Antimicrob Agents Chemother | 80 位患者隨機分組，單劑 6.5% tioconazole 軟膏 vs. 3 天 clotrimazole 陰道錠；4 週後無症狀比例 84% vs. 85%，療效相當 |
| [6347833](https://pubmed.ncbi.nlm.nih.gov/6347833/) | 1983 | RCT | Gynakol Rundsch | 雙盲比較 tioconazole 與安慰劑用於陰道念珠菌病，並評估全身吸收（無摘要） |
| [3510114](https://pubmed.ncbi.nlm.nih.gov/3510114/) | 1986 | Review | Drugs | 回顧顯示外用 tioconazole 對表淺皮膚黴菌及陰道念珠菌感染有效且安全 |
| [40464716](https://pubmed.ncbi.nlm.nih.gov/40464716/) | 2025 | Review | Expert Rev Anti Infect Ther | 探討外陰陰道念珠菌病非侵入性 azole 類藥物的未來治療選項 |
| [3984688](https://pubmed.ncbi.nlm.nih.gov/3984688/) | 1985 | 臨床研究 | Acta Obstet Gynecol Scand | 2% 陰道乳膏治療 3 天，有症狀患者黴菌學治癒率 88.5% |
| [6094282](https://pubmed.ncbi.nlm.nih.gov/6094282/) | 1984 | 隨機（開放） | J Int Med Res | 單劑外用 tioconazole 與 5 天口服 ketoconazole 比較，兩組皆有效，外用組症狀改善較快 |
| [3485546](https://pubmed.ncbi.nlm.nih.gov/3485546/) | 1986 | 開放式單組研究 | J Int Med Res | 2% 乳膏用於 20 位陰道滴蟲或混合感染患者，約 95% 治癒 |
| [3216880](https://pubmed.ncbi.nlm.nih.gov/3216880/) | 1988 | 臨床研究 | Mycoses | Tioconazole 治療陰道念珠菌病（無摘要） |
| [6347834](https://pubmed.ncbi.nlm.nih.gov/6347834/) | 1983 | 開放式比較試驗 | Gynakol Rundsch | 3 天療程 tioconazole 與 econazole 比較（無摘要） |
| [6873744](https://pubmed.ncbi.nlm.nih.gov/6873744/) | 1983 | 開放式比較試驗 | Gynakol Rundsch | Tioconazole 乳膏與 econazole 陰道栓比較（無摘要） |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-22534 | TROSYD DERMAL CREAM 1% | 乳膏 | 未提供 |
| HK-66184 | TERBUL CREAM 10MG/G | 乳膏 | 未提供 |
| HK-57887 | GYNO-ELLYCIE VAGINAL OINTMENT 6.5% | 陰道軟膏 | 未提供 |
| HK-58904 | ELLYCIE NAIL SOLUTION 28% | 指甲溶液 | 未提供 |

---

## 安全性考量

- **藥物交互作用**：已查詢到 2 筆
  - Omeprazole（嚴重度等級未知，來源 DDInter）
  - CYP8B1：Tioconazole 會抑制此人類 P450 酵素（膽酸合成路徑），屬藥理學層面的作用標的資訊

其餘警語與禁忌症請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 有 2 篇 RCT 支持其用於陰道念珠菌病，且已在香港上市。但「外陰陰道炎」實質上是原適應症的較廣泛表述，並非真正的新適應症，因此需限定範圍。
- 此決策僅適用於念珠菌引起的外陰陰道炎。

**若要推進需要：**
- 明確限定為念珠菌性外陰陰道炎，並以病原學檢查確認；非念珠菌性病因（細菌、滴蟲、萎縮性、刺激性）不應使用。
- 取得香港衛生署仿單中的警語與禁忌症資料。
- 補充詳細的作用機轉資料（MOA）。
- 補充近年的對照試驗與抗藥性（含非白色念珠菌）資料，因現有試驗多為 1980 年代的研究。

**其他預測適應症備註：**
- **外陰炎 (Vulvitis)**（分數 0.9920，證據等級 L2）：證據僅來自陰道念珠菌研究，對孤立性外陰炎屬間接證據，僅可作為研究問題；非感染性外陰炎無合理的機轉連結。
- **停經後萎縮性陰道炎**（分數 0.9919，證據等級 L5）：無文獻與臨床試驗，且病因是雌激素缺乏而非真菌感染，建議 Hold。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

