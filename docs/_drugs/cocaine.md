---
layout: default
title: Cocaine
parent: 僅模型預測 (L5)
nav_order: 220
evidence_level: L5
indication_count: 10
---

# Cocaine
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

# Cocaine：從（原適應症未載明）到 蔓延性馬尾症候群（Cauda Equina Syndrome）等預測適應症

## 一句話總結

Cocaine 是局部麻醉與血管收縮藥，香港有一張眼鼻滴劑許可證，但資料未載明核准適應症。
TxGNN 預測分數最高的新適應症是**馬尾症候群 (Cauda Equina Syndrome)**，但目前**無任何以 Cocaine 為介入藥物的臨床試驗**，文獻僅 1 篇無關的病例報告。
所有預測皆屬模型推論，多數文獻反而顯示 Cocaine 是這些症狀的**致病因子**，建議一律 Hold。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料未載明（香港許可證的核准適應症欄位為空） |
| 預測新適應症 | 馬尾症候群 (Cauda Equina Syndrome) |
| TxGNN 預測分數 | 99.98% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 1 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Cocaine 是局部麻醉劑與血管收縮劑，作用包括鈉離子通道阻斷與單胺類再攝取抑制。

馬尾症候群是壓迫性或結構性的神經病變，這兩種作用都無法治療其病因。99.98% 的高分是知識圖譜的推論，沒有臨床支持，因此**不認為此預測具有可信的治療機轉**。

其他預測適應症（見下表）也呈現相同情況：機轉不成立，或文獻顯示 Cocaine 是誘發因子。

### 其他 TxGNN 預測適應症一覽

| 排名 | 預測適應症 | 分數 | 證據等級 | 評語 |
|------|-----------|------|---------|------|
| 1 | 馬尾症候群 | 99.98% | L5 | 無合理機轉 |
| 2 | 神經性膀胱（本體論標示為過時詞條） | 99.96% | L5 | 僅預測；詞條需檢討 |
| 3 | 乳突狀結膜炎 | 99.95% | L5 | 眼部麻醉與血管收縮不改變免疫性發炎 |
| 4 | 鼻炎 | 99.92% | L4 | 文獻多為 Cocaine 引發鼻炎與黏膜壞死 |
| 5 | 大腸激躁症 | 99.89% | L5 | 無可信關聯 |
| 6 | 過敏性休克 | 99.88% | L4 | 心血管毒性使其不適用 |
| 7 | 神經循環衰弱症 | 99.83% | L5 | 擬交感作用可能惡化症狀 |
| 8 | 異位性結膜炎 | 99.83% | L5 | 相關試驗為其他藥物 |
| 9 | 食物依賴運動誘發過敏性休克 | 99.82% | L5 | 心血管風險使其不適用 |
| 10 | 咽炎 | 99.71% | L4 | 文獻多為吸食造成的咽部損傷 |

## 臨床試驗證據

馬尾症候群（排名 1）目前無相關臨床試驗登記。

以下為證據最多的「鼻炎」（排名 4）所列試驗。**這 10 項試驗皆未評估 Cocaine**，相關性分級為 C 或待定，僅供參考：

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT02953106](https://clinicaltrials.gov/study/NCT02953106) | Phase 4 | 提前終止 | 7 | 氟替卡松加氮卓斯汀鼻噴劑用於氣喘合併過敏性鼻炎；無 Cocaine |
| [NCT03549130](https://clinicaltrials.gov/study/NCT03549130) | Phase 2 | 完成 | 130 | 鼻擴張貼片對睡眠的影響（器材試驗） |
| [NCT03549117](https://clinicaltrials.gov/study/NCT03549117) | Phase 2 | 完成 | 140 | 鼻擴張貼片對慢性鼻塞與睡眠的影響 |
| [NCT01122849](https://clinicaltrials.gov/study/NCT01122849) | Phase 2 | 完成 | 61 | 鼻擴張貼片原型的探索性睡眠研究 |
| [NCT06217367](https://clinicaltrials.gov/study/NCT06217367) | Phase 4 | 未知 | 16 | 抗組織胺對被動熱壓力下體溫調節的影響 |
| [NCT07262450](https://clinicaltrials.gov/study/NCT07262450) | N/A | 招募中 | 1065 | 海水鼻噴劑的真實世界研究 |
| [NCT02745899](https://clinicaltrials.gov/study/NCT02745899) | N/A | 未知 | 100 | 牛奶攝取與兒童呼吸道症狀 |
| [NCT07527260](https://clinicaltrials.gov/study/NCT07527260) | N/A | 尚未招募 | 36 | 腺樣體／扁桃腺切除對兒童過敏性鼻炎的影響 |
| [NCT06887842](https://clinicaltrials.gov/study/NCT06887842) | N/A | 完成 | 84 | 後鼻神經切除、射頻消融與 Coblation 比較 |
| [NCT03034447](https://clinicaltrials.gov/study/NCT03034447) | N/A | 完成 | 80 | 氣喘兒童的睡眠呼吸中止與性別差異 |

其餘適應症的試驗（如異位性結膜炎的 bepotastine Phase 3 試驗）同樣是其他藥物，不構成 Cocaine 的證據。

## 文獻證據

**馬尾症候群（排名 1）**

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [31528422](https://pubmed.ncbi.nlm.nih.gov/31528422/) | 2019 | Case report | Surgical Neurology International | 遠端馬尾症候群的腰薦椎間盤病變病例與文獻回顧；與 Cocaine 治療無關 |

**鼻炎（排名 4，節選）**

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [24678064](https://pubmed.ncbi.nlm.nih.gov/24678064/) | 2014 | RCT | Int Forum Allergy Rhinol | 內視鏡鼻竇手術中，比較局部 Cocaine 與腎上腺素對術野與出血的影響（手術止血用途，非治療鼻炎） |
| [29512202](https://pubmed.ncbi.nlm.nih.gov/29512202/) | 2018 | Review | J Eur Acad Dermatol Venereol | 濫用 Cocaine 的黏膜皮膚表現 |
| [34987946](https://pubmed.ncbi.nlm.nih.gov/34987946/) | 2021 | Case report | Cureus | Cocaine 引起的腦下垂體與硬腦膜下膿瘍，慢性鼻炎為常見表現 |
| [39992969](https://pubmed.ncbi.nlm.nih.gov/39992969/) | 2025 | Case report | Medwave | 長期吸食 Cocaine 造成的硬顎穿孔 |
| [8721014](https://pubmed.ncbi.nlm.nih.gov/8721014/) | 1996 | Case series | Ear Nose Throat J | Cocaine 鼻炎的內視鏡表現 |

**過敏性休克（排名 6，節選）**

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [28863944](https://pubmed.ncbi.nlm.nih.gov/28863944/) | 2018 | Review | J Allergy Clin Immunol Pract | 藥物依賴者與過敏族群的 Cocaine 過敏，目前缺乏可靠的 IgE 檢測法 |
| [33965592](https://pubmed.ncbi.nlm.nih.gov/33965592/) | 2021 | Review | J Allergy Clin Immunol Pract | 非法藥物（含 Cocaine）的過敏與非過敏性不良反應 |
| [873631](https://pubmed.ncbi.nlm.nih.gov/873631/) | 1977 | Preclinical | Int Arch Allergy Appl Immunol | 天竺鼠肺部過敏反應中的正腎上腺素攝取 |

**咽炎（排名 10，節選）**

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [29487790](https://pubmed.ncbi.nlm.nih.gov/29487790/) | 2018 | Case report | Respir Med Case Rep | 吸入 Cocaine 後出現咽炎與嗜酸性肺炎 |
| [9149163](https://pubmed.ncbi.nlm.nih.gov/9149163/) | 1997 | Case series | Laryngoscope | 吸食 crack 或 freebase Cocaine 造成上呼吸消化道黏膜損傷 |

整體來看，文獻以「Cocaine 造成傷害」為主，屬於**危害訊號**，而非療效證據。

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-50765 | COCAINE HCL EYE/NOSE DROPS 5%（廠商：JEAN-MARIE PHARMACAL CO LTD） | 未載明（眼鼻滴劑） | 未載明 |

## 安全性考量

- **藥物交互作用**：資料庫查無記錄。

其餘警語與禁忌症資料缺漏，安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 10 個預測適應症皆為 L4–L5，沒有任何以 Cocaine 為介入藥物的臨床試驗。
- 文獻多顯示 Cocaine 會引發鼻炎、黏膜壞死、咽部損傷與過敏樣反應，屬危害訊號，且其心血管毒性使多數預測不適用。
- 已有更安全的局部麻醉劑與血管收縮劑可用。

**若要推進需要：**
- 取得香港衛生署仿單，補齊核准適應症、警語與禁忌症（目前為阻斷性資料缺口）
- 補充 DrugBank 的作用機轉資料
- 檢討「神經性膀胱」這個過時本體論詞條的映射
- 除非有新的機轉或臨床證據，否則不建議投入資源驗證這些預測

> 本報告結果僅供研究參考，不構成醫療建議。老藥新用候選需經臨床驗證後才能應用。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

