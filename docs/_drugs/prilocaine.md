---
layout: default
title: Prilocaine
parent: 高證據等級 (L1-L2)
nav_order: 415
evidence_level: L2
indication_count: 5
---

# Prilocaine
{: .fs-9 }

證據等級: **L2** | 預測適應症: **5** 個
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

# Prilocaine：從局部麻醉到神經痛（Neuralgia）

## 一句話總結

> Prilocaine 是一種 amide 類局部/區域麻醉劑，但本次評估未取得其正式核准適應症與 MOA 資料。
> TxGNN 模型針對此藥物共產出 **5 個潛在新適應症候選**，其中證據最完整、機轉最合理的是**神經痛 (Neuralgia)**，
> 目前有 **12 個臨床試驗**和 **20 篇文獻**支持，證據等級達 **L2**，是本次評估中唯一建議「附條件推進」的方向；
> 其餘 4 個候選證據等級為 L3–L5，多數缺乏機轉合理性，建議保留（Hold）或列為研究問題。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 局部/區域麻醉（香港無許可證資料，正式適應症文字缺失） |
| 預測新適應症 | 神經痛 (Neuralgia) |
| TxGNN 預測分數 | 99.34% |
| 證據等級 | L2 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Proceed with Guardrails |

---

## 所有預測候選比較

本 Evidence Pack 為多適應症候選評估（v4, multi），TxGNN 分數最高的前 3 名候選（乳頭狀結膜炎、躁狂型雙相情緒障礙、支氣管炎）雖然分數逼近 100%，但完全沒有機轉關聯或有效證據支持，判斷為知識圖譜嵌入相似性雜訊。因此本報告聚焦於**證據等級最高、決策階段最前進**的「神經痛」候選深入分析，其餘候選僅列表供對照：

| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 決策階段 | 建議 |
|------|-----------|-----------|---------|---------|------|
| 1 | Papillary conjunctivitis（乳頭狀結膜炎） | 99.78% | L5 | S0 | Hold |
| 2 | Manic bipolar affective disorder（躁狂型雙相情緒障礙） | 99.76% | L5 | S0 | Hold |
| 3 | Bronchitis（支氣管炎） | 99.64% | L5 | S0 | Hold |
| 4 | Migraine disorder（偏頭痛） | 99.42% | L3 | S1 | Research Question |
| 5 | **Neuralgia（神經痛）** | 99.34% | **L2** | **S2** | **Proceed with Guardrails** |

---

## 為什麼這個預測合理？

目前缺乏 DrugBank 結構化 MOA 資料（DG002：作用機轉資料缺口），但根據臨床試驗與文獻內容可確認：Prilocaine 為 amide 類局部麻醉劑，作用機轉為阻斷周邊感覺神經的電位依賴型 Na⁺ 通道，降低傷害性訊號傳導。

Prilocaine 最常見的臨床應用形式是與 lidocaine 組成的共熔混合物 **EMLA cream（2.5% lidocaine + 2.5% prilocaine）**，這項複方在皮膚科與疼痛科已有超過 30 年的臨床使用歷史，並多次被用於**帶狀疱疹後神經痛 (Postherpetic Neuralgia, PHN)** 及其他周邊神經病變性疼痛的止痛/去敏化治療。

神經痛與局部麻醉之間的機轉連結明確且直接：PHN 患者的疼痛主要來自受損周邊神經的異常放電與周邊敏感化，而阻斷 Na⁺ 通道正是抑制此類異常放電的標準藥理策略。這與其他 4 個候選（結膜炎、躁鬱症、支氣管炎屬純演算法雜訊；偏頭痛則屬同類藥物間接推論）相比，神經痛候選具有藥物層級的直接機轉支持，而非僅止於知識圖譜相似性推論。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00916942](https://clinicaltrials.gov/study/NCT00916942) | Phase 2 | 完成 | 20 | Lidocaine 2.5%/Prilocaine 2.5% cream 作為 NGX-4010 前置用藥，用於帶狀疱疹後神經痛(PHN)之耐受性評估 |
| [NCT01540877](https://clinicaltrials.gov/study/NCT01540877) | NA | 完成 | 28 | Capsaicin 併用局部麻醉劑之神經病變性疼痛人體實驗模型（C-fiber 阻斷與敏感化機轉） |
| [NCT03587220](https://clinicaltrials.gov/study/NCT03587220) | NA | 完成 | 44 | 局部麻醉劑（lidocaine）對 TRPV1 傷害感受去敏化機轉之研究 |
| [NCT06899438](https://clinicaltrials.gov/study/NCT06899438) | NA | 完成 | 38 | Prilocaine 與 Botulinum Toxin A 前瞻性比較治療肌筋膜疼痛症候群 |
| [NCT06247592](https://clinicaltrials.gov/study/NCT06247592) | NA | 未知 | 70 | 枕神經阻斷（使用 2% prilocaine）vs 脈衝式射頻治療慢性偏頭痛 |
| [NCT03220113](https://clinicaltrials.gov/study/NCT03220113) | Phase 1/2 | 未知 | 100 | Dexamethasone/lidocaine/thiamine 三叉神經注射治療頑固性顱顏面神經痛 |
| [NCT05411900](https://clinicaltrials.gov/study/NCT05411900) | Phase 2 | 未知 | 164 | Botulinum Toxin A 治療腕隧道症候群周邊神經病變痛 |
| [NCT01911377](https://clinicaltrials.gov/study/NCT01911377) | Phase 2 | 終止 | 12 | Botulinum Toxin A 治療脊髓損傷/多發性硬化之異感性神經痛 |
| [NCT02736890](https://clinicaltrials.gov/study/NCT02736890) | Phase 2 | 終止 | 8 | Botulinum Toxin A 皮下注射治療脊髓損傷平面疼痛 |
| [NCT07021365](https://clinicaltrials.gov/study/NCT07021365) | NA | 尚未招募 | 30 | Ganglion Impar 射頻消融 vs 酚類神經溶解術治療慢性尾骨痛（與 prilocaine 關聯性較低） |

**註：** 上表前 3 筆與 prilocaine/局部麻醉機轉直接相關；後續多筆為神經痛治療領域的其他藥物類別（Botulinum Toxin A 等）試驗，列出作為適應症治療現況參考，非 prilocaine 專一性證據。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [2493878](https://pubmed.ncbi.nlm.nih.gov/2493878/) | 1989 | RCT | BMJ | Lignocaine-prilocaine cream 對帶狀疱疹後神經痛具止痛效果 |
| [2616182](https://pubmed.ncbi.nlm.nih.gov/2616182/) | 1989 | RCT | Pain | EMLA cream 顯著改善 PHN 患者疼痛評分，含藥動學分析 |
| [10353509](https://pubmed.ncbi.nlm.nih.gov/10353509/) | 1999 | Clinical Study | Pain | EMLA 單次及重複使用皆可降低 PHN 自發性與誘發性疼痛 |
| [1430539](https://pubmed.ncbi.nlm.nih.gov/1430539/) | 1992 | Review | J Dermatol Surg Oncol | EMLA（lidocaine+prilocaine）為有效局部麻醉劑，應用範圍含 PHN 等多種適應症 |
| [23314014](https://pubmed.ncbi.nlm.nih.gov/23314014/) | 2013 | Review | Curr Opin Support Palliat Care | 慢性傷口相關疼痛之實證處置方法回顧 |
| [22182397](https://pubmed.ncbi.nlm.nih.gov/22182397/) | 2011 | Clinical Study | BMC Anesthesiol | Lidocaine/Prilocaine cream 前置用藥可提升 NGX-4010 於 PHN 患者之耐受性 |
| [2046584](https://pubmed.ncbi.nlm.nih.gov/2046584/) | 1991 | Case Report | Med J Aust | EMLA cream 用於疱疹後神經痛之病例報告 |
| [1875823](https://pubmed.ncbi.nlm.nih.gov/1875823/) | 1991 | Case Report | Med J Aust | EMLA Cream 用於疱疹後神經痛之病例報告 |
| [24310458](https://pubmed.ncbi.nlm.nih.gov/24310458/) | 2013 | Review/Case Series | Turkish Neurosurgery | 侵入性處置治療頑固性生殖股/髂腹股溝神經痛之療效評估 |
| [41777672](https://pubmed.ncbi.nlm.nih.gov/41777672/) | 2026 | Retrospective Cohort | Front Aging Neurosci | EMLA 單獨 vs 椎旁神經阻斷+EMLA，提升胸部 PHN 患者 capsaicin 貼片耐受性 |

---

## 香港上市資訊

目前無相關許可證登記。Prilocaine 在本資料集中標示為「未上市」，總許可證數為 0，無法提供品名、劑型或核准適應症資訊。

---

## 安全性考量

安全性資訊請參考原廠仿單。

（註：現有資料中主要警語、禁忌症及藥物交互作用欄位均為資料缺口，其中「仿單警語/禁忌」屬 Blocking 等級缺口，需補齊後才能進行 S1 安全性初評。）

---

## 結論與下一步

**決策：Proceed with Guardrails**（僅適用於神經痛 Neuralgia 候選）

**理由：**
- 神經痛候選具備明確、直接的機轉連結（Na⁺ 通道阻斷 → 抑制周邊神經異常放電），且有 3 篇 RCT/臨床試驗等級文獻直接支持 EMLA（lidocaine+prilocaine）用於帶狀疱疹後神經痛，證據等級達 L2，決策階段已進入 S2。
- 其餘 4 個候選中，前 3 名（乳頭狀結膜炎、躁狂型雙相情緒障礙、支氣管炎）唯一支持依據僅為 TxGNN 分數，無機轉或臨床證據，應予 **Hold**；偏頭痛候選雖有神經阻斷術類別的間接機轉關聯，但無 prilocaine 專一性證據，僅達 **Research Question** 等級。

**若要推進需要：**
- 補齊 Prilocaine 完整作用機轉（MOA）資料（DG002，High severity）
- 補齊香港仿單警語與禁忌症資料（DG001，Blocking severity，為安全性初評之必要前提）
- 確認香港是否有相關成分許可證或需新提出上市申請（目前 total_licenses = 0）
- 針對神經痛候選，建議進一步檢索 prilocaine 專一性（而非僅 EMLA 複方）之隨機對照試驗，並排除文獻中以 Botulinum Toxin A 為主要介入的間接對照研究
- 偏頭痛候選建議列為次要研究方向，待有更多 prilocaine 專一性試驗數據後再評估是否升級
- 其餘 3 個低證據候選（結膜炎、躁鬱症、支氣管炎）建議標記為 TxGNN 預測雜訊，不再投入資源追蹤
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

