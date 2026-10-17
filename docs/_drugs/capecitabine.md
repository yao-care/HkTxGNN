---
layout: default
title: Capecitabine
parent: 中證據等級 (L3-L4)
nav_order: 153
evidence_level: L3
indication_count: 10
last_modified_at: 2026-10-14
description: "Capecitabine：預測新適應症為印戒細胞胃腺癌 (Signet Ring Cell Gastric Adenocarcinoma)（證據等級 L3）。原適應症：結腸惡性腫瘤轉移、胃癌（胃腺癌、瀰漫型胃腺癌、皮革胃等）"
monitor_inn: "CAPECITABINE"
predicted_indications: ["gastric adenocarcinoma and proximal polyposis of the stomach", "signet ring cell gastric adenocarcinoma", "gastric tubular adenocarcinoma", "gastric cardia adenocarcinoma"]
---

# Capecitabine
{: .fs-9 }

證據等級: **L3** | 預測適應症: **10** 個
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

# Capecitabine：從胃癌／大腸轉移癌到胃腺癌（印戒細胞型）

## 一句話總結

Capecitabine 是口服的 5-FU 前驅藥，原本用於胃癌及結腸惡性腫瘤轉移的治療。
TxGNN 模型對多種胃部腫瘤亞型給出高分預測，本報告以證據最完整的 **印戒細胞胃腺癌 (Signet Ring Cell Gastric Adenocarcinoma)** 為主要代表。
該亞型目前有 **1 個臨床試驗**和 **20 篇文獻**，但多為病例報告與回溯研究。證據最強的是**胃管狀腺癌**（多項 Phase 3 RCT），不過這屬於原適應症內的標準用法，並非真正的再利用。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 結腸惡性腫瘤轉移、胃癌（胃腺癌、瀰漫型胃腺癌、皮革胃等） |
| 預測新適應症 | 印戒細胞胃腺癌 (Signet Ring Cell Gastric Adenocarcinoma) |
| TxGNN 預測分數 | 99.94% |
| 證據等級 | L3 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Hold（印戒細胞亞型）；胃管狀腺癌與賁門腺癌可 Proceed with Guardrails |

> 排名第 1 的預測為「胃腺癌合併胃近端息肉病 (GAPPS)」，目前沒有任何臨床試驗或文獻，僅為模型預測（L5）。

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Capecitabine 是 5-FU 的口服前驅藥，屬於氟嘧啶類（fluoropyrimidine）藥物，在體內轉換為 5-FU 後抑制胸苷酸合成酶（thymidylate synthase），干擾 DNA 合成。這一機轉在胃癌中的療效已被證實，因此機轉上可能適用於胃癌的各種組織學亞型。

印戒細胞癌是胃腺癌的一種組織學亞型，而胃腺癌本身屬於原適應症。因此預測在疾病分類上高度合理。不過，印戒細胞型一般被認為對化療較不敏感，亞型專屬的療效仍不確定。

同一批高分預測中，多數是胃癌的解剖部位或分子亞型（賁門、胃體、幽門、EBV 相關、管狀腺癌等），本質上與原適應症重疊。相對地，惡性胃顆粒細胞瘤屬於罕見的間質性腫瘤，與胃腺癌差異較大，與 Capecitabine 的關聯薄弱。

---

## 臨床試驗證據

### 印戒細胞胃腺癌

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT07091227](https://clinicaltrials.gov/study/NCT07091227) | Phase 2 | 尚未招募 | 66 | AK112 合併化療作為含印戒細胞之胃／胃食道交界腺癌的術前治療；Capecitabine 的角色未於標題中確認，僅為薄弱的支持證據 |

### 其他亞型的重點試驗（賁門腺癌）

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00040859](https://clinicaltrials.gov/study/NCT00040859) | Phase 2 | 完成 | 48 | Oxaliplatin 加 Capecitabine 用於轉移性食道、胃食道交界及賁門腺癌，直接測試 Capecitabine |
| [NCT00938470](https://clinicaltrials.gov/study/NCT00938470) | Phase 2 | 完成 | 73 | 局部晚期食道／胃食道交界／賁門腺癌的延長術前治療（含 Capecitabine 的方案） |
| [NCT01295086](https://clinicaltrials.gov/study/NCT01295086) | N/A | 完成 | 27 | 劑量探索：Docetaxel、Oxaliplatin、Capecitabine 加 Trastuzumab 用於 HER2 陽性晚期食道／賁門／胃癌 |

### 其他亞型的重點試驗（胃體癌）

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT02494583](https://clinicaltrials.gov/study/NCT02494583) | Phase 3 | 完成 | 763 | Pembrolizumab 單用或合併 Cisplatin 加 5-FU／Capecitabine 的第一線治療；Capecitabine 的角色需再確認 |

---

## 文獻證據

### 印戒細胞胃腺癌

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [35085931](https://pubmed.ncbi.nlm.nih.gov/35085931/) | 2022 | Cohort | Eur J Cancer | 比較 FLOT 與 MAGIC（含 Capecitabine）圍手術期化療對局部晚期食道胃腺癌的存活影響 |
| [39237045](https://pubmed.ncbi.nlm.nih.gov/39237045/) | 2025 | Phase 1 | Int J Radiat Oncol Biol Phys | 短程放化療作為可切除胃癌全程新輔助治療的安全性與毒性 |
| [34000769](https://pubmed.ncbi.nlm.nih.gov/34000769/) | 2021 | Retrospective cohort | Zhonghua Wei Chang Wai Ke Za Zhi | 真實世界中胃癌圍手術期化療對預後的影響 |
| [20721843](https://pubmed.ncbi.nlm.nih.gov/20721843/) | 2010 | Review | Dtsch Med Wochenschr | 胃癌的診斷與治療概述 |
| [26324361](https://pubmed.ncbi.nlm.nih.gov/26324361/) | 2015 | Review | J Clin Oncol | 局部胃腺癌先手術後的輔助治療選擇 |
| [26848413](https://pubmed.ncbi.nlm.nih.gov/26848413/) | 2015 | Case report | Cureus | 印戒細胞胃癌復發，以 ECX（含 Capecitabine）化療加多器官切除 |

### 胃管狀腺癌（證據最強）

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [22226517](https://pubmed.ncbi.nlm.nih.gov/22226517/) | 2012 | RCT (Phase 3) | Lancet | CLASSIC：D2 胃切除後輔助 Capecitabine 加 Oxaliplatin 改善無病存活 |
| [34252374](https://pubmed.ncbi.nlm.nih.gov/34252374/) | 2021 | RCT (Phase 3) | Lancet Oncol | RESOLVE：SOX 對比術後 CapeOx 用於局部晚期胃癌 |
| [39952264](https://pubmed.ncbi.nlm.nih.gov/39952264/) | 2025 | RCT (Phase 3) | Lancet Oncol | RESOLVE 最終報告，含整體存活更新 |
| [30982686](https://pubmed.ncbi.nlm.nih.gov/30982686/) | 2019 | RCT (Phase 2/3) | Lancet | FLOT4：FLOT 對比 ECF／ECX（含 Capecitabine）的圍手術期治療 |
| [37524953](https://pubmed.ncbi.nlm.nih.gov/37524953/) | 2023 | RCT (Phase 3) | Nat Med | GLOW：Zolbetuximab 加 CAPOX 用於 CLDN18.2 陽性胃癌 |
| [34102137](https://pubmed.ncbi.nlm.nih.gov/34102137/) | 2021 | RCT (Phase 3) | Lancet | CheckMate 649：Nivolumab 加化療的第一線治療 |

### 其他亞型的重點文獻

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [16303863](https://pubmed.ncbi.nlm.nih.gov/16303863/) | 2006 | Phase 2 | Ann Oncol | Oxaliplatin 加 Capecitabine 用於轉移性食道、胃食道交界及賁門腺癌（賁門） |
| [42026044](https://pubmed.ncbi.nlm.nih.gov/42026044/) | 2026 | Phase 2 | Nat Commun | 新輔助 Toripalimab 加 CapeOX 用於 EBV 相關胃癌（17 例）（EBV 相關） |
| [18665164](https://pubmed.ncbi.nlm.nih.gov/18665164/) | 2008 | Phase 2 RCT | Br J Cancer | Capecitabine 對比 S-1 用於高齡晚期胃癌（胃體） |
| [36051651](https://pubmed.ncbi.nlm.nih.gov/36051651/) | 2022 | Case report | Case Rep Surg | AFP 產生型胃癌肝轉移以 Capecitabine／Oxaliplatin 治療成功（幽門） |

---

## 香港上市資訊

Capecitabine 在香港共有 20 張有效許可證，皆為單一成分製劑，無已註銷者。下表列出 5 張主要許可證。

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-46233 | XELODA TAB 150MG（原廠，DKSH） | 錠劑 | 本次資料未提供 |
| HK-62914 | CAPECITABINE SANDOZ TABLET 500MG | 錠劑 | 本次資料未提供 |
| HK-63404 | CAPECITABINE-TEVA FILM-COATED TABLETS 500MG | 膜衣錠 | 本次資料未提供 |
| HK-68949 | CAPECITABINE TABLETS 500MG（Viatris） | 錠劑 | 本次資料未提供 |
| HK-66278 | PACSITA TABLETS 500MG | 錠劑 | 本次資料未提供 |

其餘許可證涵蓋 150 mg 與 500 mg 規格，品牌包括 FACIVIX、INTACAPE、ACCORD 等。

---

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 傳統細胞毒性藥物（氟嘧啶類，5-FU 前驅藥） |
| 骨髓抑制風險 | 中度。知識圖譜顯示對嗜中性白血球低下、血小板低下、無顆粒球症、貧血等族群有禁忌關聯 |
| 致吐性分級 | 低至中度（依藥物類別判斷） |
| 監測項目 | CBC（含分類）、肝功能（膽紅素）、腎功能 |
| 處置防護 | 需依細胞毒性藥物處置規範操作 |

具 DPD（二氫嘧啶脫氫酶）缺乏者風險特別高，使用前應考慮相關評估。詳細警語請參考原廠仿單。

---

## 安全性考量

- **禁忌／高風險族群（來自知識圖譜關聯，非仿單原文）**：肝病、膽囊疾病、血小板低下、嗜中性白血球低下、無顆粒球症、貧血（含巨球性貧血）、高膽紅素血症（含吉爾伯特氏症候群）、腎功能不全、冠狀動脈疾病、心臟傳導疾病、猝死性心臟停止、感染性疾病、壞死性小腸結腸炎、口腔炎、DPD 缺乏症。
- **藥物交互作用**：資料庫共記錄 100 筆，以下為部分：
  - 中度：Metronidazole、Tinidazole
  - 輕度：Aluminum hydroxide、Levofloxacin、Magaldrate、Magnesium carbonate／hydroxide／oxide
  - 等級未知：Pantoprazole、Omeprazole、Lansoprazole、Metformin、Simvastatin、Prednisone 等

香港仿單的警語與禁忌尚未取得，正式使用前請務必查閱原廠仿單。

---

## 結論與下一步

**決策：Hold（印戒細胞亞型）；胃管狀腺癌、賁門腺癌、胃體癌為 Proceed with Guardrails**

**理由：**
- 印戒細胞胃腺癌雖有高 TxGNN 分數，但唯一的試驗尚未招募且 Capecitabine 角色不明，文獻以病例報告與回溯研究為主，且該亞型化療敏感度可能較低，目前只能視為研究問題。
- 胃管狀腺癌有多項 Phase 3 RCT（如 CLASSIC、RESOLVE）支持，但這屬於原適應症的標準用法，並非真正的再利用。賁門腺癌有已完成的 Phase 2 支持。
- GAPPS、微侵襲性胃癌、惡性胃顆粒細胞瘤僅有模型預測，證據不足，建議 Hold。

**若要推進需要：**
- 取得香港衛生署仿單的警語與禁忌症
- 補充 Capecitabine 的作用機轉資料
- 釐清印戒細胞型的亞型專屬療效（重新分析既有 Phase 3 試驗中的亞組資料）
- 確認納入試驗中 Capecitabine 的實際角色（如 NCT07091227、NCT02494583）
- 建立 DPD 缺乏篩檢與血液學監測計畫
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

