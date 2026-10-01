---
layout: default
title: Tacrolimus
parent: 僅模型預測 (L5)
nav_order: 830
evidence_level: L5
indication_count: 3
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

<div id="pharmacist">

## 藥師評估報告

</div>

# Tacrolimus：從異位性皮膚炎與器官移植到脂漏性皮膚炎

## 一句話總結

Tacrolimus 是鈣調磷酸酶（calcineurin）抑制劑，外用藥膏用於異位性皮膚炎，口服膠囊用於器官移植後的免疫抑制。
TxGNN 模型預測它可能對**脂漏性皮膚炎 (Seborrheic Dermatitis)** 有效。
目前有 **2 個臨床試驗**（Phase 3 與 Phase 4，皆已完成）和 **20 篇文獻**，其中約 5 篇是直接以 tacrolimus 治療脂漏性皮膚炎的臨床研究。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 脂漏性皮膚炎 (Seborrheic Dermatitis) |
| TxGNN 預測分數 | 99.26% |
| 證據等級 | L2（依判定規則；說明見下方） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Proceed with Guardrails |

> 證據包內的許可證資料未附原適應症文字，因此本表省略「原適應症」。
> 證據等級：只有 1 個已完成的 Phase 3 RCT（NCT02004860），不滿足 L1 所需的 ≥2 個。
> 文獻中的雙盲 RCT（PMID 33010323）可能與該 Phase 3 試驗是同一研究，所以不重複計算，判為 L2。

## 為什麼這個預測合理？

證據包沒有提供 Tacrolimus 的作用機轉（MOA）資料。以下說明依據一般藥理知識。Tacrolimus 抑制鈣調磷酸酶，阻斷 NFAT 依賴的 T 細胞活化，減少 IL-2 等促發炎細胞介質的釋放。

脂漏性皮膚炎是慢性、反覆發作的發炎性皮膚病，好發於臉部與頭皮，發炎反應是病程的重要部分。抑制 T 細胞介導的發炎，與外用 tacrolimus 在異位性皮膚炎的作用基礎相同，因此機轉上說得通。部分文獻也提到它可能對馬拉色菌（Malassezia）有抗黴作用，但目前資料無法證實。

臨床上，傳統外用類固醇不適合長期用在臉部，而鈣調磷酸酶抑制劑被視為替代選項。多篇文獻（如 PMID 19222250）討論了這個用途。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT02004860](https://clinicaltrials.gov/study/NCT02004860) | Phase 3 | 完成 | 120 | Protopic（tacrolimus 藥膏）用於成人臉部重度脂漏性皮膚炎的維持治療，目標是減少復發、延長緩解期、減少外用類固醇使用 |
| [NCT01591070](https://clinicaltrials.gov/study/NCT01591070) | Phase 4 | 完成 | 104 | 0.1% tacrolimus 藥膏每週 1–2 次的主動式（proactive）治療，評估能否維持成人臉部脂漏性皮膚炎緩解並減少惡化 |

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [33010323](https://pubmed.ncbi.nlm.nih.gov/33010323/) | 2021 | RCT（多中心、雙盲） | J Am Acad Dermatol | 0.1% tacrolimus 對比 1% ciclopiroxolamine，用於重度臉部脂漏性皮膚炎的維持治療 |
| [26512166](https://pubmed.ncbi.nlm.nih.gov/26512166/) | 2015 | 臨床試驗 | Ann Dermatol | 0.1% tacrolimus 藥膏用於臉部脂漏性皮膚炎的維持治療 |
| [24171300](https://pubmed.ncbi.nlm.nih.gov/24171300/) | 2013 | 比較性臨床試驗 | Ann Parasitol | 60 位患者，比較 2% sertaconazole 乳膏與 0.03% tacrolimus 乳膏的療效 |
| [37067129](https://pubmed.ncbi.nlm.nih.gov/37067129/) | 2023 | 比較性臨床研究 | Indian J Dermatol Venereol Leprol | 越南研究，比較口服 itraconazole 2 天加外用 tacrolimus 與單用外用 tacrolimus 的維持治療 |
| [12833030](https://pubmed.ncbi.nlm.nih.gov/12833030/) | 2003 | 開放式先導研究 | J Am Acad Dermatol | 18 位患者使用 0.1% tacrolimus，11 位（61%）達到 100% 清除 |
| [19222250](https://pubmed.ncbi.nlm.nih.gov/19222250/) | 2009 | Review | Am J Clin Dermatol | 回顧外用鈣調磷酸酶抑制劑治療脂漏性皮膚炎的病理機轉、安全性與療效，認為是類固醇之外的安全替代選項 |
| [27804089](https://pubmed.ncbi.nlm.nih.gov/27804089/) | 2017 | 系統性回顧 | Am J Clin Dermatol | 臉部脂漏性皮膚炎外用治療的系統性回顧 |
| [19213227](https://pubmed.ncbi.nlm.nih.gov/19213227/) | 2009 | Review | J Drugs Dermatol | 臉部脂漏性皮膚炎的現況與治療展望 |
| [11770914](https://pubmed.ncbi.nlm.nih.gov/11770914/) | 2001 | Review | Semin Cutan Med Surg | 外用 tacrolimus 與 pimecrolimus 的未來方向，涵蓋脂漏性皮膚炎等其他皮膚疾病 |

## 香港上市資訊

香港已有 20 張含 tacrolimus 的許可證，以下列出 5 張。證據包未提供劑型與核准適應症文字。品名顯示同時有口服膠囊與外用藥膏（0.03%）產品。

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-68880 | TACCORDERM OINTMENT 0.03% W/W | JACOBSON MARKETING LIMITED |
| HK-61877 | TACROLIMUS-TEVA CAPSULES 0.5MG | TEVA PHARMACEUTICAL HONG KONG |
| HK-68422 | TACROLIMUS CAPSULES USP 1MG | DCH AURIGA (HONG KONG) LIMITED |
| HK-58356 | TACROLIMUS SANDOZ CAP 1MG | SANDOZ HONG KONG LIMITED |
| HK-47471 | PROGRAF CAP 0.5MG | ASTELLAS PHARMA HONG KONG |

## 安全性考量

安全性資訊請參考原廠仿單。證據包中的警語與禁忌症皆無資料，藥物交互作用查詢也無結果。

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 有 1 個已完成的 Phase 3 試驗、1 個 Phase 4 試驗，加上至少一項雙盲 RCT，都直接針對脂漏性皮膚炎的維持治療，機轉上也合理。
- 香港仿單的警語與禁忌症資料缺失，無法完成安全性篩選，因此只能附帶防護條件推進。

**防護條件：**
- 僅限外用，並注意外用鈣調磷酸酶抑制劑類別的黑框警語。
- 脂漏性皮膚炎在多數地區可能屬於仿單外使用（off-label）。
- 臉部避免未經評估的長期連續使用。

**若要推進需要：**
- 取得香港衛生署的仿單，確認警語、禁忌症與核准適應症（DG001，屬阻擋性缺口）。
- 補充 DrugBank 的作用機轉資料（DG002）。
- 確認 NCT02004860 與 PMID 33010323 是否為同一研究，並取得兩者的主要療效數據。
- 評估外用藥膏長期使用於臉部的安全性。

> 本報告僅供研究參考，不構成醫療建議；預測結果需經臨床驗證。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

