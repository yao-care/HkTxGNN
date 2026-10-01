---
layout: default
title: Tioconazole
parent: 高證據等級 (L1-L2)
nav_order: 865
evidence_level: L2
indication_count: 3
---

# Tioconazole
{: .fs-9 }

證據等級: **L2** | 預測適應症: **3** 個
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

# Tioconazole：從（原適應症未載明）到外陰陰道炎

## 一句話總結

Tioconazole 是咪唑類（imidazole）抗黴菌藥，香港有 4 張外用製劑許可證，但證據包中未載明原適應症。
TxGNN 模型預測它可能對**外陰陰道炎 (Vulvovaginitis)** 有效，目前有 **2 個臨床試驗**和 **20 篇文獻**支持，其中包含 2 篇 tioconazole 本身的 RCT。
這比較像是已有文獻支持的既有用途（念珠菌性陰道炎），不是典型的老藥新用。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 許可證資料未提供 |
| 預測新適應症 | 外陰陰道炎 (Vulvovaginitis) |
| TxGNN 預測分數 | 99.23% |
| 證據等級 | L2 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 4 張 |
| 建議決策 | Proceed with Guardrails |

## 為什麼這個預測合理？

目前缺乏詳細的 DrugBank 作用機轉資料。根據藥理分類，Tioconazole 是咪唑類抗黴菌藥，抑制黴菌的羊毛固醇 14-α 去甲基酶（CYP51），阻斷麥角固醇合成，破壞黴菌細胞膜。念珠菌是外陰陰道炎最主要的病原，因此機轉上與此適應症直接相關。

文獻也顯示 tioconazole 早已用於外陰陰道念珠菌症，包括單次劑量 6.5% 軟膏及 2% 陰道乳膏。這很可能屬於**標示內用途**，不是真正的老藥新用，需對照香港許可證的核准適應症確認。

這個預測只適用於**念珠菌性**外陰陰道炎。目前沒有證據支持它用於細菌性陰道病。滴蟲性陰道炎僅有一個 20 人的開放性單臂研究（見下方文獻）。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT06056947](https://clinicaltrials.gov/study/NCT06056947) | Phase 3 | 完成 | 577 | Fenticonazole + Tinidazole + Lidocaine 不同劑型 vs Gynomax® XL，用於細菌性陰道病、念珠菌性外陰陰道炎、滴蟲性陰道炎及混合感染。藥物並非 tioconazole，僅支持唑類藥物的類別合理性 |
| [NCT03839875](https://clinicaltrials.gov/study/NCT03839875) | Phase 4 | 完成 | 116 | Gynomax® XL 陰道栓劑的開放性單臂研究，適應症同上。藥物並非 tioconazole，無對照組，僅為間接證據 |

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [3524439](https://pubmed.ncbi.nlm.nih.gov/3524439/) | 1986 | RCT | Antimicrob Agents Chemother | 80 人隨機分組，單次 6.5% tioconazole 軟膏 vs 3 日 clotrimazole 陰道錠；4 週後無症狀率 84% vs 85%，療效相當 |
| [6347833](https://pubmed.ncbi.nlm.nih.gov/6347833/) | 1983 | RCT | Gynakol Rundsch | 雙盲、安慰劑對照，評估 tioconazole 治療陰道念珠菌症的療效、耐受性、安全性及全身吸收 |
| [3510114](https://pubmed.ncbi.nlm.nih.gov/3510114/) | 1986 | Review | Drugs | Tioconazole 對皮癬菌和酵母菌有廣效抗菌活性；開放與對照試驗顯示外用製劑治療淺層黴菌感染和陰道念珠菌症有效且安全 |
| [40464716](https://pubmed.ncbi.nlm.nih.gov/40464716/) | 2025 | Review | Expert Rev Anti Infect Ther | 回顧外陰陰道念珠菌症的非侵入性唑類抗黴菌治療選項與未來方向 |
| [10470518](https://pubmed.ncbi.nlm.nih.gov/10470518/) | 1999 | Review | Compr Ther | 健康女性外陰陰道炎的流行病學、診斷與治療回顧 |
| [6094282](https://pubmed.ncbi.nlm.nih.gov/6094282/) | 1984 | 隨機開放試驗 | J Int Med Res | 40 人，單次 6% tioconazole 陰道軟膏 vs 口服 ketoconazole 5 天；兩組皆有效，局部治療症狀緩解較快 |
| [6873744](https://pubmed.ncbi.nlm.nih.gov/6873744/) | 1983 | 開放性比較試驗 | Gynakol Rundsch | Tioconazole 乳膏 vs econazole 陰道栓劑，3 日療程治療陰道念珠菌症 |
| [6347834](https://pubmed.ncbi.nlm.nih.gov/6347834/) | 1983 | 開放性比較試驗 | Gynakol Rundsch | Tioconazole vs econazole，3 日療程治療陰道念珠菌症 |
| [3984688](https://pubmed.ncbi.nlm.nih.gov/3984688/) | 1985 | 臨床研究 | Acta Obstet Gynecol Scand | 29 名有症狀婦女使用 2% 陰道乳膏，黴菌學治癒率 88.5% |
| [3485546](https://pubmed.ncbi.nlm.nih.gov/3485546/) | 1986 | 開放性單臂研究 | J Int Med Res | 20 名滴蟲性或混合感染患者使用 2% 乳膏 3 天，首次追蹤治癒率 95% (19/20) |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-22534 | TROSYD DERMAL CREAM 1% | 乳膏（依品名） | 資料未提供 |
| HK-66184 | TERBUL CREAM 10MG/G | 乳膏（依品名） | 資料未提供 |
| HK-57887 | GYNO-ELLYCIE VAGINAL OINTMENT 6.5% | 陰道軟膏（依品名） | 資料未提供 |
| HK-58904 | ELLYCIE NAIL SOLUTION 28% | 甲用溶液（依品名） | 資料未提供 |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
Tioconazole 對念珠菌性外陰陰道炎有 2 篇自身 RCT 與多篇比較研究支持，機轉合理，且香港已有陰道軟膏上市。但這些研究多為 1980 年代，且證據僅限於念珠菌性。Phase 3 與 Phase 4 試驗用的是其他唑類藥物，不是直接證據。許可證的核准適應症與安全性資料也都缺漏。

**若要推進需要：**
- 取得香港衛生署仿單，確認陰道軟膏（HK-57887）的核准適應症與警語、禁忌，判斷這是標示內用途還是真正的新適應症
- 補齊 DrugBank 作用機轉資料
- 將適用範圍限定在念珠菌性外陰陰道炎，非念珠菌性感染不納入
- 外陰炎（rank 2，L3）缺乏以外陰炎為終點的研究，且可能由非黴菌因素引起，僅列為研究問題
- 停經後萎縮性陰道炎（rank 3，L5）缺乏機轉依據與任何研究證據，建議 Hold，高分可能只是知識圖譜上與其他陰道炎相近所致

*本報告結果僅供研究參考，不構成醫療建議；老藥新用候選需經臨床驗證才能應用。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

