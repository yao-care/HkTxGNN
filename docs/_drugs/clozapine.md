---
layout: default
title: Clozapine
parent: 高證據等級 (L1-L2)
nav_order: 188
evidence_level: L2
indication_count: 10
---

# Clozapine
{: .fs-9 }

證據等級: **L2** | 預測適應症: **10** 個
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

# Clozapine：從治療抗藥性精神分裂症到躁鬱性情感障礙（躁症發作）

## 一句話總結

Clozapine 是第二代（非典型）抗精神病藥，全球主要適應症為治療抗藥性精神分裂症（treatment-resistant schizophrenia）。
TxGNN 模型預測它可能對**躁鬱性情感障礙躁症發作（Manic Bipolar Affective Disorder）** 有效，
目前有 **6 個臨床試驗**和 **20 篇文獻**支持這個方向。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 治療抗藥性精神分裂症（國際通用適應症；香港無核准登記） |
| 預測新適應症 | 躁鬱性情感障礙躁症發作（Manic Bipolar Affective Disorder） |
| TxGNN 預測分數 | 99.95% |
| 證據等級 | L2 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

Clozapine 屬於多受體靶向非典型抗精神病藥（MARTA），其藥理特徵為對 D2、D4、5-HT2A、α1/α2、H1 及 M1-M5 受體均具有親和力。尤其對 D4 受體的高度親和力與 5-HT2A 拮抗作用，是其有別於傳統抗精神病藥的關鍵所在。目前缺乏完整的正式 MOA 資料，但根據 Evidence Pack 中的機轉分析，D2 受體的過度阻斷可抑制躁症發作時多巴胺迴路的過度活性，而 5-HT2A 拮抗則有助於穩定情緒波動。

躁鬱症躁症發作（尤其是治療抗藥性躁症）與精神分裂症在神經生物學上共享多巴胺過度活躍的病理基礎。事實上，Clozapine 的抗躁效果並非全新假設——1990 年代即已有案例報告，2000 年代後陸續有系統性回顧及隨機對照試驗嘗試評估其療效，特別是針對「傳統藥物（鋰鹽、丙戊酸鹽、第二代抗精神病藥）無效」的難治性躁狂患者。

此外，Clozapine 具有已被 FDA 批准的抗自殺效果（適應症為精神分裂症族群），而躁鬱症患者的自殺風險為一般人口的 25 倍。其抗衝動與抗攻擊特性（經由 5-HT2A 及 α2 受體介導）在躁症急性期的行為控制上具有潛在優勢，進一步支持此適應症的合理性。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00029458](https://clinicaltrials.gov/study/NCT00029458) | Phase 2 | 已完成 | 42 | 雙盲研究，直接評估 Clozapine 用於治療抗藥性躁狂發作的安全性與有效性 |
| [NCT05603104](https://clinicaltrials.gov/study/NCT05603104) | Phase 3 | 招募中 | 1,254 | 強化藥物治療 vs 常規治療，涵蓋精神分裂症、重度憂鬱及躁鬱憂鬱族群，首次治療失敗後的介入研究 |
| [NCT07047651](https://clinicaltrials.gov/study/NCT07047651) | Phase 4 | 招募中 | 40 | 藥物合併新型復元導向心理治療（RECOVERYTRSBDGR）用於治療抗藥性躁鬱症 |
| [NCT03651674](https://clinicaltrials.gov/study/NCT03651674) | N/A | 不明 | 200 | ECT 對精神分裂症及躁鬱症的縱向 MRI 研究，探討腦結構功能變化及 ECT 反應預測標記 |
| [NCT06993662](https://clinicaltrials.gov/study/NCT06993662) | Phase 1 | 積極進行（不再招募） | 107 | 藥物合併個別認知行為治療於多種精神疾病之復元導向研究 |
| [NCT07398365](https://clinicaltrials.gov/study/NCT07398365) | N/A | 招募中 | 100 | NHS 一般成人精神科住院病人醫療表型研究，提供精神病合併內科疾病發生率基礎資料 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [32182485](https://pubmed.ncbi.nlm.nih.gov/32182485/) | 2020 | 系統性回顧＋統合分析 | J Psychiatr Res | 評估 Clozapine 用於躁鬱症的臨床療效與副作用，為目前最高等級證據 |
| [33719158](https://pubmed.ncbi.nlm.nih.gov/33719158/) | 2021 | 回顧 | Bipolar Disord | 彙整 Clozapine 用於躁鬱症現有知識，討論未來研究方向 |
| [25346322](https://pubmed.ncbi.nlm.nih.gov/25346322/) | 2015 | 系統性回顧 | Bipolar Disord | 評估 Clozapine 用於治療抗藥性躁鬱症（TRBD）之療效與安全性 |
| [37068038](https://pubmed.ncbi.nlm.nih.gov/37068038/) | 2023 | 藥物流行病學研究 | J Clin Psychopharmacol | 亞洲精神藥物處方模式聯盟（含台灣）之 Clozapine 用於躁鬱症實際使用分析 |
| [40174308](https://pubmed.ncbi.nlm.nih.gov/40174308/) | 2025 | 真實世界回顧性世代研究 | J Psychiatr Res | 韓國全國健保資料庫分析 Clozapine、鋰鹽、丙戊酸鹽於精神分裂症及躁鬱症患者的抗自殺效果 |
| [31488793](https://pubmed.ncbi.nlm.nih.gov/31488793/) | 2019 | 回顧 | Psychiatria Danubina | 探討 Clozapine 獨特藥理特性（抗攻擊、抗衝動）對躁鬱症自殺防治的潛在效益 |
| [33460070](https://pubmed.ncbi.nlm.nih.gov/33460070/) | 2020 | 回顧 | Acta Psychiatr Scand | 躁症發作的實證治療建議，涵蓋心境穩定劑與抗精神病藥物的選擇 |
| [16432528](https://pubmed.ncbi.nlm.nih.gov/16432528/) | 2006 | 回顧 | Mol Psychiatry | 難治性躁鬱症的藥物治療策略，Clozapine 被列為替代療法之一 |
| [11280956](https://pubmed.ncbi.nlm.nih.gov/11280956/) | 2001 | 回顧 | Bull Menninger Clin | 難治性躁鬱症的早期藥物選擇綜述，包含 Clozapine 等非典型抗精神病藥 |
| [10682225](https://pubmed.ncbi.nlm.nih.gov/10682225/) | 2000 | 病例系列回顧 | Clin Neuropharmacol | 回顧 36 例 ECT 合併 Clozapine 治療（適應症包含抗藥性病例），67% 患者有效 |

---

## 香港上市資訊

Clozapine 在香港目前**無核准藥物許可證**（根據本 Evidence Pack 資料）。

> 臨床使用如需取得 Clozapine，需透過香港醫院管理局特殊藥物申請（Special Drug Application）或個別醫院的治療抗藥性精神病用藥計畫，並遵循血液監測規程（因顆粒球缺乏症風險）。

---

## 安全性考量

安全性資訊請參考原廠仿單。

> **重要提醒**：Clozapine 為全球已知具有**顆粒球缺乏症（agranulocytosis）**高風險的抗精神病藥物，所有使用者均需定期接受白血球計數監測。此外，可能引發癲癇（劑量相關）、心肌炎、代謝症候群及過度鎮靜。以上風險在躁鬱症族群的具體安全性資料有待 TFDA 仿單資料補充驗證。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
已有系統性回顧與統合分析（Tier 1）及一項 Phase 2 雙盲完成試驗直接支持 Clozapine 用於治療抗藥性躁鬱症躁症發作，且亞洲地區（含台灣）亦有真實世界處方使用的藥物流行病學資料，證據強度達 L2，機轉關聯性充分，具備推進條件。但 Clozapine 在香港無現有許可證，且具有嚴重安全性疑慮（顆粒球缺乏症），需在嚴格監控條件下進行。

**若要推進需要：**
- 補充完整作用機轉（MOA）資料（查詢 DrugBank API，當前為 Data Gap）
- 下載並解析 TFDA/香港衛生署原廠仿單，完成安全性初評（S1 阻斷項）
- 建立血液學監測計畫（CBC 含分類計數，尤其顆粒球/嗜中性球）
- 評估香港本地是否有難治性躁鬱症患者的未滿足醫療需求，確認目標病人族群
- 考慮透過香港醫院管理局「特殊用藥申請」機制作為初期引進路徑

---

> ⚠️ **免責聲明**：本報告結果僅供研究參考，不構成醫療建議。老藥新用候選需經過完整臨床驗證方可應用於臨床。
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

