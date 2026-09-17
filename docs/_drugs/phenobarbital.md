---
layout: default
title: Phenobarbital
parent: 僅模型預測 (L5)
nav_order: 576
evidence_level: L5
indication_count: 5
---

# Phenobarbital
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# PHENOBARBITAL：癲癇相關反射性/誘發性適應症多重預測評估

## 一句話總結

PHENOBARBITAL（苯巴比妥，DrugBank DB01174）目前香港未上市，證據包中亦缺乏其正式核准適應症與作用機轉的結構化資料。TxGNN 模型針對此藥物提出 **5 個候選新適應症**（三叉神經腫瘤、進食性癲癇、聽源性癲癇、性高潮誘發性癲癇、思考誘發性癲癇），預測分數均逼近 **99.96%**，但實際查證後**僅 1 個候選（進食性癲癇）達到「Research Question」等級**，其餘 4 個因證據薄弱、族群錯配或屬本體映射雜訊而維持 **Hold**。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 無資料（Evidence Pack 未提供已核准適應症文字，`original_indications` 與 `original_moa` 均為資料缺口） |
| 香港上市 | 未上市 |
| 許可證數 | 0 張 |

| 排名 | 預測新適應症 | TxGNN 分數 | TxGNN 排名 | 證據等級 | 決策階段 | 建議決策 |
|------|-------------|-----------|-----------|---------|---------|---------|
| 1 | 三叉神經腫瘤 (Trigeminal Nerve Neoplasm) | 99.96% | 1165 | L5 | S0 | Hold |
| 2 | 進食性癲癇 (Eating Seizures) | 99.96% | 1206 | L4 | S1 | **Research Question** |
| 3 | 聽源性癲癇 (Audiogenic Seizures) | 99.96% | 1207 | L4 | S0 | Hold |
| 4 | 性高潮誘發性癲癇 (Orgasm-induced Seizures) | 99.96% | 1208 | L5 | S0 | Hold |
| 5 | 思考誘發性癲癇 (Thinking Seizures) | 99.96% | 1209 | L4 | S0 | Hold |

---

## 為什麼這個預測合理？

目前缺乏 PHENOBARBITAL 詳細的結構化作用機轉資料（DrugBank MOA 欄位為資料缺口，DG002）。但從各候選適應症的機轉推論文字中可看出一致的藥理邏輯：**苯巴比妥是典型的 GABA-A 受體正向調節劑**，透過延長氯離子通道開放時間、提高癲癇閾值，是廣效型抗癲癇藥（AED），臨床上早已用於控制多種型態的癲癇發作。

這也是本次預測結果的關鍵解讀重點：TxGNN 找到的 5 個候選中，**除「三叉神經腫瘤」明顯是知識圖譜疾病本體映射錯誤**（唯一引用文獻談的是 Sturge-Weber 症候群，一種伴隨癲癇的神經皮膚疾病，推測被誤配到三叉神經腫瘤節點，非真實腫瘤治療證據）之外，其餘 4 個（進食性、聽源性、性高潮誘發性、思考誘發性癲癇）**本質上都是反射性癲癇（reflex epilepsy）的亞型**，而苯巴比妥作為廣效 AED，機轉上對各type反射性癲癇皆有理論基礎。換言之，這批預測比較像是「模型重新發現苯巴比妥已知的抗癲癇效果，並精確定位到特定反射性癲癇亞型」，而非發現全新的治療領域。

真正的問題在於**這些亞型是否有直接的人體對照試驗證據**，而非機轉是否合理——目前答案是否定的，多數證據仍停留在動物模型與個案報告層級。

---

## 臨床試驗證據

目前無相關臨床試驗登記（5 個候選適應症的 ClinicalTrials.gov 與 ICTRP 查詢皆為 0 筆）。

---

## 文獻證據

### 1. 三叉神經腫瘤（L5）

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [9157801](https://pubmed.ncbi.nlm.nih.gov/9157801/) | 1997 | Case Series | Anales españoles de pediatría | 回顧 14 例 Sturge-Weber 症候群，與三叉神經腫瘤無直接關聯，疑為本體映射雜訊 |

### 2. 進食性癲癇（L4，Research Question）

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [24726506](https://pubmed.ncbi.nlm.nih.gov/24726506/) | 2014 | Case Report（50年追蹤） | Seizure | 新生兒進食性癲癇個案，50 年長期追蹤 |
| [7259585](https://pubmed.ncbi.nlm.nih.gov/7259585/) | 1981 | 個案報告 | Arquivos de neuro-psiquiatria | 進食誘發癲癇個案，以 valproate＋clonazepam＋phenobarbital 併用獲最佳控制 |
| [2105880](https://pubmed.ncbi.nlm.nih.gov/2105880/) | 1990 | Animal Study | Epilepsia | 苯巴比妥長期投予對自發性癲癇大鼠（SER）之強直性發作有明顯抑制效果 |
| [8422850](https://pubmed.ncbi.nlm.nih.gov/8422850/) | 1993 | 藥動學研究 | Epilepsia | 兒童併用 carbamazepine 與 phenobarbital 之藥動學比較 |
| [9579909](https://pubmed.ncbi.nlm.nih.gov/9579909/) | 1997 | Case Report | Epilepsia | AED 減量誘發之陰性肌躍狀態，3 例報告 |
| [3128813](https://pubmed.ncbi.nlm.nih.gov/3128813/) | 1988 | Animal Study | Psychopharmacology | 苯巴比妥對沙鼠生殖表現與後代發育之不良影響 |
| [11064963](https://pubmed.ncbi.nlm.nih.gov/11064963/) | 2000 | 個案報告 | J Dev Behav Pediatr | 幼兒進食問題、睡眠障礙與負面行為之發展行為評估個案 |
| [21711263](https://pubmed.ncbi.nlm.nih.gov/21711263/) | 2011 | 綜述 | Acta Neurol Scand Suppl | 癲癇成人骨骼健康：phenobarbital 等肝酶誘導型 AED 與骨折風險相關 |
| [6095778](https://pubmed.ncbi.nlm.nih.gov/6095778/) | 1984 | 藥理研究 | Arch Int Pharmacodyn Ther | 新型喹啉衍生物於腦內苯二氮平受體之部分激動劑特性研究 |
| [3996884](https://pubmed.ncbi.nlm.nih.gov/3996884/) | 1985 | 動物實驗 | General Pharmacology | 餵食方式對大鼠電擊與 metrazole 誘發癲癇反應之影響 |

**評語**：僅有 2 篇個案報告直接涉及「進食誘發癲癇」且合併使用苯巴比妥，其餘多為 AED 一般性藥動/安全性研究，尚無對照試驗。

### 3. 聽源性癲癇（L4）

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [19735986](https://pubmed.ncbi.nlm.nih.gov/19735986/) | 2010 | Case Report | Brain & Development | 高劑量苯巴比妥治療後嬰兒West症候群之痙攣消失，但聽源性癲癇與非驚厥性癲癇重積持續 |
| [26690830](https://pubmed.ncbi.nlm.nih.gov/26690830/) | 2017 | RCT（獸醫） | J Feline Med Surg | 貓聽源反射性癲癇：levetiracetam 與 phenobarbital 隨機對照，療效相近 |
| [7327097](https://pubmed.ncbi.nlm.nih.gov/7327097/) | 1981 | Animal Study | Developmental Neuroscience | 早期暴露苯巴比妥使小鼠聽源性癲癇易感性顯著降低（僅10%癲癇發作） |
| [9592113](https://pubmed.ncbi.nlm.nih.gov/9592113/) | 1998 | Animal Study | J Neuroscience | 鎂缺乏誘發聽源性癲癇小鼠模型，作為抗癲癇藥篩選平台 |
| [23872084](https://pubmed.ncbi.nlm.nih.gov/23872084/) | 2013 | Animal Study | Epilepsy & Behavior | GASH倉鼠模型比較 phenobarbital、valproic acid、levetiracetam 之藥理與神經行為效果 |
| [17150334](https://pubmed.ncbi.nlm.nih.gov/17150334/) | 2006 | Animal Study | Epilepsy Research | Wistar聽源性癲癇大鼠腦區EEG小波分析與抗癲癇藥效果 |
| [27663280](https://pubmed.ncbi.nlm.nih.gov/27663280/) | 2016 | Animal Study | Eur J Pharmacol | 大麻素類化合物增強多種AED（含phenobarbital）對DBA/2小鼠聽源性癲癇之保護作用 |
| [11284448](https://pubmed.ncbi.nlm.nih.gov/11284448/) | 2001 | Animal Study | Naunyn-Schmiedeberg's Arch Pharmacol | Retigabine增強phenobarbital等AED對DBA/2小鼠聽源性癲癇之抗癲癇活性 |
| [10863138](https://pubmed.ncbi.nlm.nih.gov/10863138/) | 2000 | Animal Study | Epilepsy Research | D-cycloserine增強phenobarbital等AED對聽源性癲癇之保護效果 |
| [14288355](https://pubmed.ncbi.nlm.nih.gov/14288355/) | 1965 | Animal Study | J Comp Physiol Psychol | 皮質擴散抑制與藥物對大鼠聽源性癲癇之作用 |

**評語**：唯一具人體資料的是 1 篇嬰兒個案報告；僅有的 RCT 為獸醫（貓）研究，其餘皆為 DBA/2 小鼠等動物模型，屬機轉支持證據而非臨床證據。

### 4. 性高潮誘發性癲癇

目前無相關文獻。

### 5. 思考誘發性癲癇（L4）

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [27057183](https://pubmed.ncbi.nlm.nih.gov/27057183/) | 2016 | RCT（族群為熱性痙攣，非思考誘發性癲癇，適應症錯配） | Iran J Child Neurol | 間歇性 diazepam 與連續性 phenobarbital 預防熱性痙攣復發之隨機對照試驗 |
| [37655702](https://pubmed.ncbi.nlm.nih.gov/37655702/) | 2023 | Guideline/Review | Epilepsia | ILAE新生兒癲癇治療共識指引，含phenobarbital用藥建議 |
| [23515971](https://pubmed.ncbi.nlm.nih.gov/23515971/) | 2013 | Systematic Review | CNS Drugs | 兒童局部癲癇藥物治療系統性回顧 |
| [25112558](https://pubmed.ncbi.nlm.nih.gov/25112558/) | 2014 | Animal Study | Epilepsy & Behavior | 新生兒期短暫暴露苯巴比妥損害大鼠被動迴避學習與感覺運動閘控能力 |
| [29940514](https://pubmed.ncbi.nlm.nih.gov/29940514/) | 2018 | Animal Study | Epilepsy Research | Phenobarbital、phenytoin、pregabalin三藥併用於小鼠強直陣攣癲癇模型之等辜線分析 |
| [21777642](https://pubmed.ncbi.nlm.nih.gov/21777642/) | 2011 | Animal Study | Prog Neuropsychopharmacol Biol Psychiatry | 合成大麻素WIN 55,212-2對phenobarbital等AED抗PTZ誘發陣攣性癲癇之保護作用之影響 |
| [18379717](https://pubmed.ncbi.nlm.nih.gov/18379717/) | 2008 | Animal Study | J Neural Transm | Agmatine增強phenobarbital與valproate於小鼠最大電擊癲癇模型之抗癲癇作用 |
| [15525996](https://pubmed.ncbi.nlm.nih.gov/15525996/) | 2005 | Animal Study | Neuropsychopharmacology | Vigabatrin與phenobarbital等傳統AED於PTZ誘發癲癇之交互作用等辜線分析 |
| [26738990](https://pubmed.ncbi.nlm.nih.gov/26738990/) | 2016 | Animal Study | Neurochemical Research | Mexiletine與phenobarbital等傳統AED之交互作用等辜線分析 |
| [8545459](https://pubmed.ncbi.nlm.nih.gov/8545459/) | 1995 | Animal Study | Pharmacol Biochem Behav | AED對點燃(kindling)誘發癲癇及其認知損害之影響 |

**評語**：唯一的 RCT（PMID 27057183）研究族群為熱性痙攣，與「思考誘發性癲癇」不符，屬適應症錯配；其餘為指引性引用或動物機轉研究，無直接針對此亞型的臨床證據。

---

## 香港上市資訊

PHENOBARBITAL 目前**未在香港取得任何藥品許可證**（`total_licenses = 0`），Evidence Pack 中無許可證品名、劑型或核准適應症資料可供列出。

---

## 安全性考量

安全性資訊請參考原廠仿單。

> 補充說明：本評估的資料缺口清單將「TFDA 仿單警語/禁忌」列為 **Blocking** 等級缺口（DG001），已直接導致所有候選適應症無法進入 S1 安全性初評（僅「進食性癲癇」因臨床證據較充分而例外進入 S1）。在補齊仿單資料前，不應將任何候選適應症推進至下一階段。

---

## 結論與下一步

**決策：Hold**（「進食性癲癇」候選可標記為 Research Question，其餘 4 個維持 Hold）

**理由：**
- 5 個候選中有 1 個（三叉神經腫瘤）經核實為知識圖譜疾病本體映射雜訊，非真實訊號。
- 其餘 4 個雖有合理的 GABA-A 機轉支持，但證據幾乎全數來自動物模型；僅有的人體 RCT（PMID 27057183）族群為熱性痙攣，與目標適應症「思考誘發性癲癇」不符。
- 安全性資料（仿单警語、禁忌症、DDI）與正式 MOA 皆為 Blocking／High 等級資料缺口，且藥物在香港未上市，缺乏在地監管路徑。

**若要推進需要：**
- 補齊 DG001：向 TFDA／原廠取得完整仿單警語與禁忌症，解除 S1 安全性初評的封鎖。
- 補齊 DG002：透過 DrugBank API 取得正式 MOA，強化機轉關聯性分析的可信度。
- 針對「進食性癲癇」候選，優先檢索是否有更新的人體病例系列或小型前瞻性研究，確認其 Research Question 定位是否可再升級。
- 釐清苯巴比妥是否已具有「癲癇／反射性癲癇」的既有核准適應症——若是，這批預測的本質應定位為「亞型精準化」而非「全新適應症」，需調整後續開發策略的框架。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

