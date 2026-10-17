---
layout: default
title: Tacrolimus
parent: 僅模型預測 (L5)
nav_order: 845
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-14
description: "Tacrolimus：預測新適應症為脂漏性皮膚炎 (Seborrheic Dermatitis)（證據等級 L5）。原適應症：異位性皮膚炎（atopic eczema / atopic dermatitis）"
monitor_inn: "TACROLIMUS"
predicted_indications: ["parapsoriasis"]
---

# Tacrolimus
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

# Tacrolimus：從異位性皮膚炎到脂漏性皮膚炎

## 一句話總結

Tacrolimus 是鈣調磷酸酶（calcineurin）抑制劑，原本用於異位性皮膚炎（atopic eczema）。
TxGNN 模型預測它可能對**脂漏性皮膚炎 (Seborrheic Dermatitis)** 有效，
目前有 **2 個臨床試驗**（其中 1 個為已完成的 Phase 3）和 **20 篇文獻**支持這個方向。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 異位性皮膚炎（atopic eczema / atopic dermatitis） |
| 預測新適應症 | 脂漏性皮膚炎 (Seborrheic Dermatitis) |
| TxGNN 預測分數 | 99.26% |
| 證據等級 | L2（僅 1 個已完成的 Phase 3 試驗，且為單一試驗；另有 1 個 Phase 4） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Proceed with Guardrails |

> 註：本報告所編纂的資料中，香港許可證的核准適應症文字皆為空白，原適應症係依知識圖譜的適應症關聯填寫。

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知的藥理知識，tacrolimus 是鈣調磷酸酶抑制劑，會抑制 T 細胞活化及促發炎細胞激素的釋放。外用劑型已被用於異位性皮膚炎，而其局部免疫調節作用也是這類藥物的核心特性。

脂漏性皮膚炎是一種慢性、反覆發作的發炎性皮膚病，好發於臉部與頭皮等皮脂腺豐富的區域。一般認為與皮膚上的馬拉色菌（Malassezia）所引發的免疫發炎反應有關。由於兩種疾病都涉及 T 細胞參與的皮膚發炎，抑制鈣調磷酸酶在機轉上有合理的適用性。文獻也指出，外用鈣調磷酸酶抑制劑可作為脂漏性皮膚炎中，長期使用類固醇的替代選擇。

此外，已有 Phase 3 試驗直接檢驗外用 tacrolimus 於嚴重臉部脂漏性皮膚炎的維持治療，與預測方向一致。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT02004860](https://clinicaltrials.gov/study/NCT02004860) | Phase 3 | 已完成 | 120 | 評估 tacrolimus 軟膏（Protopic）用於成人臉部嚴重脂漏性皮膚炎的維持治療，目標是減少復發、延長緩解期並減少外用類固醇使用 |
| [NCT01591070](https://clinicaltrials.gov/study/NCT01591070) | Phase 4 | 已完成 | 104 | 評估每週 1–2 次主動式（proactive）使用 0.1% tacrolimus 軟膏，能否維持成人臉部脂漏性皮膚炎的緩解並減少惡化 |

> 上述試驗登記資料僅提供試驗設計與目的，未包含結果數據。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [27804089](https://pubmed.ncbi.nlm.nih.gov/27804089/) | 2017 | 系統性回顧 | Am J Clin Dermatol | 臉部脂漏性皮膚炎外用治療的系統性回顧，涵蓋抗黴菌劑、角質溶解劑與類固醇等類別 |
| [26512166](https://pubmed.ncbi.nlm.nih.gov/26512166/) | 2015 | 臨床研究 | Ann Dermatol | 以 0.1% tacrolimus 軟膏作為臉部脂漏性皮膚炎的維持治療 |
| [19222250](https://pubmed.ncbi.nlm.nih.gov/19222250/) | 2009 | Review | Am J Clin Dermatol | 外用鈣調磷酸酶抑制劑治療脂漏性皮膚炎的病理機轉、安全性與療效回顧，認為是類固醇之外的安全替代選擇 |
| [19213227](https://pubmed.ncbi.nlm.nih.gov/19213227/) | 2009 | Review | J Drugs Dermatol | 臉部脂漏性皮膚炎的現況與治療展望 |
| [17685874](https://pubmed.ncbi.nlm.nih.gov/17685874/) | 2007 | Review | Expert Opin Investig Drugs | 外用 tacrolimus 的新角色，包含在其他皮膚疾病的應用 |
| [15461548](https://pubmed.ncbi.nlm.nih.gov/15461548/) | 2004 | Review | Expert Opin Pharmacother | 外用 tacrolimus 用於異位性皮膚炎及其他發炎性皮膚病 |
| [11770914](https://pubmed.ncbi.nlm.nih.gov/11770914/) | 2001 | Review | Semin Cutan Med Surg | 外用 tacrolimus 與 pimecrolimus 的未來方向，包含脂漏性皮膚炎等應用 |
| [31476936](https://pubmed.ncbi.nlm.nih.gov/31476936/) | 2019 | Review | J Cutan Med Surg | 外用鈣調磷酸酶抑制劑於皮膚科仿單外用途的證據整理 |
| [24171300](https://pubmed.ncbi.nlm.nih.gov/24171300/) | 2013 | 臨床試驗 | Ann Parasitol | 比較 2% sertaconazole 乳膏與 0.03% tacrolimus 乳膏治療脂漏性皮膚炎（60 名患者） |
| [16094289](https://pubmed.ncbi.nlm.nih.gov/16094289/) | 2005 | 觀察性研究 | Nihon Ishinkin Gakkai Zasshi | 脂漏性與異位性皮膚炎患者的馬拉色菌菌種分析 |

## 香港上市資訊

香港共有 20 張有效的單一成分許可證，涵蓋口服膠囊（速釋與緩釋）及外用軟膏。以下列出 5 張主要許可證；資料中未提供劑型與核准適應症文字。

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-48907 | PROTOPIC OINT 0.03%（DKSH Hong Kong） | 軟膏 | 未提供 |
| HK-47471 | PROGRAF CAP 0.5MG（Astellas） | 膠囊 | 未提供 |
| HK-56596 | ADVAGRAF PROLONGED-RELEASE HARD CAP 0.5MG（Astellas） | 緩釋膠囊 | 未提供 |
| HK-61331 | REMUS OINTMENT 0.1%W/W（Unipharm） | 軟膏 | 未提供 |
| HK-65222 | TACROZ OINTMENT 0.03% W/W（SB Pharma） | 軟膏 | 未提供 |

## 細胞毒性

Tacrolimus 屬免疫抑制劑（鈣調磷酸酶抑制劑），非傳統抗腫瘤細胞毒性藥物，故不適用本章節。

## 安全性考量

- **知識圖譜標示的禁忌或風險疾病**（非仿單內容）：高血壓、長 QT 症候群與尖端扭轉型心律不整、肝衰竭、腎臟疾病、癲癇、高血糖與糖尿病（含酮酸中毒）、感染性疾病（含單純疱疹、帶狀疱疹、傳染性單核球增多症、慢性 EB 病毒感染）、癌症與淋巴瘤（含原發性中樞神經淋巴瘤）、進行性多灶性白質腦病、後部白質腦病變症候群、譫妄、再生不良性貧血等。這些多與全身性（口服/注射）使用的風險相關，外用情境需由臨床判斷。
- **藥物交互作用**：共查得 100 筆，以下為部分例子。
  - 嚴重（Major）：Amphotericin B、Loperamide、Mesalazine、Omeprazole、Balsalazide
  - 中度（Moderate）：Acarbose、Famotidine、Rabeprazole、Hydrocortisone、Metformin、Pioglitazone、Aprepitant、Triamcinolone、Dexamethasone、Betamethasone、Metronidazole、Budesonide 等
- **外用長期使用的疑慮**：外用鈣調磷酸酶抑制劑有惡性腫瘤方面的警語。2023 年一篇系統性回顧與統合分析（PMID 36370744）針對此議題評估了異位性皮膚炎患者的癌症風險。

香港仿單的警語與禁忌資料尚未取得，請參考原廠仿單。

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 已有 1 個已完成的 Phase 3 試驗（n=120）與 1 個已完成的 Phase 4 試驗（n=104）直接檢驗外用 tacrolimus 於脂漏性皮膚炎，且機轉上與 T 細胞介導的皮膚發炎相符，外用劑型已在香港上市。但這兩個試驗的結果數據未納入本次資料，證據等級以 L2 保守判定。

**若要推進需要：**
- 取得 NCT02004860 與 NCT01591070 的實際療效與安全性結果
- 取得香港仿單的警語、禁忌與核准適應症文字（目前缺口，屬阻擋性項目）
- 補充詳細的作用機轉資料
- 制定長期外用的安全監測計畫（含惡性腫瘤與感染風險），並確認此用途屬仿單外使用的溝通方式
- 針對併用藥物（尤其是 CYP3A4 相關交互作用）建立檢核機制

---

**其他預測適應症（供參考）**

- **類副牛皮癬（Parapsoriasis，預測分數 99.24%）**：僅有 2 篇個案報告（外用 tacrolimus 治療苔癬樣糠疹），無臨床試驗，證據等級 L4，建議 **Hold**。
- **皮膚炎（Dermatitis，預測分數 99.17%）**：此類別主要為異位性皮膚炎，屬已核准的既有適應症，並非真正的再利用，已有多個 Phase 3 試驗與統合分析支持，證據等級 L1。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

